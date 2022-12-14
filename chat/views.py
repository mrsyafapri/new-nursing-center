from django.conf import settings
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication

from users.models import User
from chat.serializers import MessageModelSerializer
from chat.models import Message


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class MessagePagination(PageNumberPagination):
    page_size = settings.MESSAGES_TO_LOAD


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer
    allowed_methods = ("GET", "POST", "HEAD", "OPTIONS")
    authentication_classes = (CsrfExemptSessionAuthentication,)
    pagination_class = MessagePagination

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(
            Q(recipient=request.user) | Q(user=request.user)
        )
        target = self.request.query_params.get("target", None)
        if target is not None:
            self.queryset = self.queryset.filter(
                Q(recipient=request.user, user__username=target)
                | Q(recipient__username=target, user=request.user)
            )
        return super(MessageModelViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        msg = get_object_or_404(
            self.queryset.filter(
                Q(recipient=request.user) | Q(user=request.user), Q(pk=kwargs["pk"])
            )
        )
        serializer = self.get_serializer(msg)
        return Response(serializer.data)


class ChatView(TemplateView):
    template_name = "chat/index.html"

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        context["is_doctor"] = self.request.user.is_doctor
        context["patients"] = User.objects.filter(
            is_doctor=False, is_superuser=False
        ).exclude(id=self.request.user.id)
        context["doctors"] = User.objects.filter(
            is_doctor=True, is_superuser=False
        ).exclude(id=self.request.user.id)
        return context
