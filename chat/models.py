from django.conf import settings
from django.db import models
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class MessageModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="user",
        related_name="from_user",
        db_index=True,
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="recipient",
        related_name="to_user",
        db_index=True,
    )
    timestamp = models.DateTimeField(
        "timestamp", auto_now_add=True, editable=False, db_index=True
    )
    body = models.TextField("body")

    def __str__(self):
        return str(self.id)

    def characters(self):
        return len(self.body)

    def notify_ws_clients(self):
        notification = {
            "type": "recieve_group_message",
            "message": "{}".format(self.id),
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)(
            "{}".format(self.recipient.id), notification
        )

    def save(self, *args, **kwargs):
        new = self.id
        self.body = self.body.strip()  # Trimming whitespaces from the body
        super(MessageModel, self).save(*args, **kwargs)
        if new is None:
            self.notify_ws_clients()

    class Meta:
        app_label = "chat"
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ("-timestamp",)
