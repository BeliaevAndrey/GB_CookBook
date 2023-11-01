from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class LoginUser(CreateView):
    """ User register view """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login.html'


class RegisterUser(CreateView):
    """ User register view """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'signup.html'
