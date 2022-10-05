from django.contrib.auth.forms import UserCreationForm

from users.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "avatar",
            "email",
            "phone_number",
            "address",
            "id_card",
            "password1",
            "password2",
        )
