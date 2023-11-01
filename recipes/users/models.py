from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Extension of builtin user model.
    (By materials from django.fun article:
    https://django.fun/ru/articles/tips/polzovatelskaya-model-user/)
    """
    pass    # not other fields needed yet
