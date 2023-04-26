from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Subscribe(models.Model):
    class Status(models.TextChoices):
        subscribe = 'subscribe', _('عضو شده')
        unsubscribe = 'unsubscribe', _('عضو نشده')
    email = models.EmailField(verbose_name=_("ایمیل"), max_length=254)
    date_joined = models.DateTimeField(verbose_name=_("تاریخ عضویت"), auto_now=False, auto_now_add=False)
    status = models.CharField(verbose_name=_("وضعیت"), max_length=50, choices=Status.choices, default=Status.unsubscribe)
    class Meta:
        verbose_name = _("ایمیل")
        verbose_name_plural = _("ایمیل ها")
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.email