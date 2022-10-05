from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return super().get(request)

    def get_success_url(self):
        return "/login/"
