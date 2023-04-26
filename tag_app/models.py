from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class TagModel(models.Model):
    name = models.CharField(max_length=160, verbose_name=_("نام تگ"))
    slug = models.CharField(max_length=160, verbose_name=_("اسلاک تگ"), unique=True)
    date_created = models.DateTimeField(auto_now_add=False, verbose_name=_("تاریخ ایجاد"))
    
    class Meta:
        verbose_name = _("تگ")
        verbose_name_plural = _(" تگ ها")
    
    def __str__(self):
        return self.name
        