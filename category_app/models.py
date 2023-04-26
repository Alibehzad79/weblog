from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=160, verbose_name=_("نام دسته بندی"))
    slug = models.CharField(max_length=160, verbose_name=_("اسلاک دسته بندی"), unique=True)
    image = models.ImageField(verbose_name=_("تصویر"), upload_to='images/category/')
    date_created = models.DateTimeField(auto_now_add=False, verbose_name=_("تاریخ ایجاد"))
    
    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _(" دسته بندی ها")
    
    def __str__(self):
        return self.name