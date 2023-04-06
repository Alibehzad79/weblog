from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class AboutModel(models.Model):
    title = models.CharField(verbose_name=_("عنوان",), max_length=50)
    content = RichTextField(verbose_name=_("محتوا"))
    date_created = models.DateTimeField(auto_now_add=False, verbose_name=_('تاریخ ایجاد'))

    class Meta:
        verbose_name = _("درباره ما")
        verbose_name_plural = _("درباره ما")

    def __str__(self):
        return self.title