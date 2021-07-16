from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):  # Modelform for registration
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name")
