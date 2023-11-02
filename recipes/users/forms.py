from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email']
        labels = {
            'username': 'Имя',
            'email': 'Email',
            'password1': 'pwd',
            'password2': 'cnm pwd',
        }
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', ]
        labels = {
            'username': 'Имя',
            'email': 'Email',
            'password1': 'pwd',
            'password2': 'cnm pwd',
        }
