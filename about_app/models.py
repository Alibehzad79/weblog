from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import html
# Create your models here.

class AboutModel(models.Model):
    title = models.CharField(verbose_name=_("عنوان",), max_length=50)
    content = RichTextField(verbose_name=_("محتوا"))
    date_created = models.DateTimeField(auto_now_add=False, verbose_name=_('تاریخ ایجاد'))
    description = models.CharField(verbose_name=_("توضیحات"), max_length=160, help_text=_("160 character | SEO"))
    keywords = models.TextField(verbose_name=_("کلمات کلیدی"), help_text=_("با , از هم جدا کنید | SEO"))
    
    class Meta:
        verbose_name = _("درباره ما")
        verbose_name_plural = _("درباره ما")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("about:about")
    
    def get_description(self):
        if self.description is not '':
            return html.format_html(f'<meta name="description" content="{self.description}">')
        
    def get_keywords(self):
        if self.keywords is not '':
            return html.format_html(f'<meta name="keywords" content="{self.keywords}">')
