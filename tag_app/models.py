from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import html
# Create your models here.

class TagModel(models.Model):
    name = models.CharField(max_length=160, verbose_name=_("نام تگ"))
    slug = models.CharField(max_length=160, verbose_name=_("اسلاک تگ"), unique=True)
    date_created = models.DateTimeField(auto_now_add=False, verbose_name=_("تاریخ ایجاد"))
    description = models.CharField(verbose_name=_("توضیحات"), max_length=160, help_text=_("160 character | SEO"))
    keywords = models.TextField(verbose_name=_("کلمات کلیدی"), help_text=_("با , از هم جدا کنید | SEO"))
        
    class Meta:
        verbose_name = _("تگ")
        verbose_name_plural = _(" تگ ها")
    
    def __str__(self):
        return self.name
    
    def get_description(self):
        if self.description is not '':
            return html.format_html(f'<meta name="description" content="{self.description}">')
        
    def get_keywords(self):
        if self.keywords is not '':
            return html.format_html(f'<meta name="keywords" content="{self.keywords}">')
