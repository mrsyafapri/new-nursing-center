from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static

from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chat.urls")),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("signup/", user_views.SignupView.as_view(), name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
