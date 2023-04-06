from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name=_('ایمیل'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']