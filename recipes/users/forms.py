from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta(UserCreationForm):
        email = forms.EmailField()
        model = CustomUser
        fields = ['username', 'email', 'password']


class CustomUserChangeForm(UserChangeForm):
    # email = forms.EmailField()

    class Meta:
        email = forms.EmailField()
        model = CustomUser
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    """ User welcome form """
    pass


class RegisterForm(forms.Form):
    """ User register form"""
    pass
