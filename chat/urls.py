from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

from chat.views import (
    MessageModelViewSet,
    ChatView,
)

router = DefaultRouter()
router.register(r"message", MessageModelViewSet, basename="message-api")

urlpatterns = [
    path(r"api/v1/", include(router.urls)),
    path(
        "",
        login_required(ChatView.as_view()),
        name="home",
    ),
]
