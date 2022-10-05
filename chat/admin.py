from django.contrib import admin

from chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ("timestamp",)
    search_fields = ("id", "body", "user__username", "recipient__username")
    list_display = ("id", "user", "recipient", "timestamp", "characters")
    list_display_links = ("id",)
    list_filter = ("user", "recipient")
    date_hierarchy = "timestamp"


admin.site.register(Message, MessageAdmin)
