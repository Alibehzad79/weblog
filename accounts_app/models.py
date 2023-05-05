from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name=_("ایمیل"), max_length=254, unique=True)
    forget_password_hash = models.CharField(verbose_name=_("forget password hash"), max_length=64, blank=True, null=True)