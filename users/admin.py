from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Doctor


class UserAdminConfig(UserAdmin):
    model = User
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "address",
                    "id_card",
                    "avatar",
                    "is_doctor",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "address",
                    "id_card",
                    "avatar",
                    "is_doctor",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Doctor)
