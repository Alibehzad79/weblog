from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.urls import reverse
# Create your models here.

class ContactModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("عنوان"))
    date_created = models.DateTimeField(auto_now_add=False, verbose_name=_("تاریخ ایجاد"))
    
    class Meta:
        verbose_name=_("توضیح")
        verbose_name_plural=_("صفحه تماس با ما")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("contact:contact")


class ContactModelForm(models.Model):
    class Status(models.TextChoices):
        read = 'read', _("جواب داد شده")
        unread = 'unread', _("جواب داد نشده")
    name = models.CharField(verbose_name=_("نام"), max_length=50)
    email = models.EmailField(verbose_name=_("ایمیل"), max_length=254)
    subject = models.CharField(verbose_name=_("عنوان تماس"), max_length=50)
    text = models.TextField(verbose_name=_("متن تماس"))
    date_sent = models.DateTimeField(verbose_name=_("تاریخ ارسال"), auto_now=False, auto_now_add=False)
    answre = models.TextField(verbose_name=_("جواب"), blank=True, null=True)
    status = models.CharField(verbose_name=_("وضعیت"), max_length=50, choices=Status.choices, default=Status.unread)
    class Meta:
        verbose_name = _("تماس")
        verbose_name_plural = _("تماس های کاربران")
        
    def __str__(self):
        return self.email

class Telephone(models.Model):
    contact = models.ForeignKey(ContactModel, on_delete=models.DO_NOTHING, verbose_name=_("تماس با ما"), related_name="telephones")
    phone = models.CharField(verbose_name=_("شماره تلفن"), max_length=20)    

class Email(models.Model):
    contact = models.ForeignKey(ContactModel, on_delete=models.DO_NOTHING, verbose_name=_("تماس با ما"), related_name="emails")
    email = models.EmailField(verbose_name=_("ایمیل"))    
  
class Address(models.Model):
    contact = models.ForeignKey(ContactModel, on_delete=models.DO_NOTHING, verbose_name=_("تماس با ما"), related_name="addresses")
    address = models.CharField(verbose_name=_("آدرس"), max_length=150)    
        