from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from blog_app.models import ArticleModel
from about_app.models import AboutModel
from contact_app.models import ContactModel
# Create your models here.
class ArticlePageAdsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class AboutPageAdsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class ContactPageAdsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class HomePageAdsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)




class ArticlePageAds(models.Model):
    creator = models.ForeignKey(get_user_model(), verbose_name=_("سازنده تبلیغ"), on_delete=models.DO_NOTHING, related_name='article_adses')
    article = models.ForeignKey(ArticleModel, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING, related_name='ads')
    title = models.CharField(verbose_name=_("عنوان"), max_length=100)
    url = models.URLField(verbose_name=_("لینک"), max_length=200, help_text=_("https://..."))
    file = models.ImageField(verbose_name=_("فایل"), upload_to="files/ads/", help_text=_("نوع فایل: گیف"))
    date_created = models.DateTimeField(verbose_name=_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    expiry_date = models.DateTimeField(verbose_name=_("تاریخ انقضاء"), auto_now=False, auto_now_add=False)
    pay = models.CharField(verbose_name=_("هزینه پرداختی"), max_length=100)
    active = models.BooleanField(verbose_name=_("فعال"))
    
    objects = ArticlePageAdsManager()
    class Meta:
        verbose_name=_("تبلیغ")
        verbose_name_plural=_("تبلیغات صفحه های مقاله ها")
    
    def __str__(self):
        return self.title


class AboutPageAds(models.Model):
    creator = models.ForeignKey(get_user_model(), verbose_name=_("سازنده تبلیغ"), on_delete=models.DO_NOTHING, related_name='about_adses')
    about = models.ForeignKey(AboutModel, verbose_name=_("درباره ما"), on_delete=models.DO_NOTHING, related_name='ads')
    title = models.CharField(verbose_name=_("عنوان"), max_length=100)
    url = models.URLField(verbose_name=_("لینک"), max_length=200, help_text=_("https://..."))
    file = models.ImageField(verbose_name=_("فایل"), upload_to="files/ads/", help_text=_("نوع فایل: گیف"))
    date_created = models.DateTimeField(verbose_name=_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    expiry_date = models.DateTimeField(verbose_name=_("تاریخ انقضاء"), auto_now=False, auto_now_add=False)
    pay = models.CharField(verbose_name=_("هزینه پرداختی"), max_length=100)
    active = models.BooleanField(verbose_name=_("فعال"))
    
    objects = AboutPageAdsManager()
    class Meta:
        verbose_name=_("تبلیغ")
        verbose_name_plural=_("تبلیغات صفحه درباره ما")
    
    def __str__(self):
        return self.title

class ContactPageAds(models.Model):
    creator = models.ForeignKey(get_user_model(), verbose_name=_("سازنده تبلیغ"), on_delete=models.DO_NOTHING, related_name='contact_adses')
    contact = models.ForeignKey(ContactModel, verbose_name=_("درباره ما"), on_delete=models.DO_NOTHING, related_name='ads')
    title = models.CharField(verbose_name=_("عنوان"), max_length=100)
    url = models.URLField(verbose_name=_("لینک"), max_length=200, help_text=_("https://..."))
    file = models.ImageField(verbose_name=_("فایل"), upload_to="files/ads/", help_text=_("نوع فایل: گیف"))
    date_created = models.DateTimeField(verbose_name=_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    expiry_date = models.DateTimeField(verbose_name=_("تاریخ انقضاء"), auto_now=False, auto_now_add=False)
    pay = models.CharField(verbose_name=_("هزینه پرداختی"), max_length=100)
    active = models.BooleanField(verbose_name=_("فعال"))
    
    objects = ContactPageAdsManager()
    class Meta:
        verbose_name=_("تبلیغ")
        verbose_name_plural=_("تبلیغات صفحه تماس ما")
    
    def __str__(self):
        return self.title

class HomePageAds(models.Model):
    creator = models.ForeignKey(get_user_model(), verbose_name=_("سازنده تبلیغ"), on_delete=models.DO_NOTHING, related_name='home_adses')
    title = models.CharField(verbose_name=_("عنوان"), max_length=100)
    url = models.URLField(verbose_name=_("لینک"), max_length=200, help_text=_("https://..."))
    file = models.ImageField(verbose_name=_("فایل"), upload_to="files/ads/", help_text=_("نوع فایل: گیف"))
    date_created = models.DateTimeField(verbose_name=_("تاریخ ایجاد"), auto_now=False, auto_now_add=False)
    expiry_date = models.DateTimeField(verbose_name=_("تاریخ انقضاء"), auto_now=False, auto_now_add=False)
    pay = models.CharField(verbose_name=_("هزینه پرداختی"), max_length=100)
    active = models.BooleanField(verbose_name=_("فعال"))
    
    objects = HomePageAdsManager()
    class Meta:
        verbose_name=_("تبلیغ")
        verbose_name_plural=_("تبلیغات صفحه خانه")
    
    def __str__(self):
        return self.title    