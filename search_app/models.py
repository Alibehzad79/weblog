from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Search(models.Model):
    query_name = models.CharField(verbose_name=_("کلمه"), max_length=150)
    search_count = models.BigIntegerField(default=0, verbose_name=_("تعداد سرچ"))
    date_created = models.DateTimeField(verbose_name=_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    date_updated = models.DateTimeField(verbose_name=_("آخرین آپدیت"), auto_now=False, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.query_name
    
    class Meta:
        verbose_name = _("نتیجه")
        verbose_name_plural = _("نتایچ سرچ")
        ordering = ['-date_updated']