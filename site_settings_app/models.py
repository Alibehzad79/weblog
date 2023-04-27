from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Setting(models.Model):
    site_name = models.CharField(verbose_name=_("نام سایت"), max_length=50)
    site_address = models.URLField(verbose_name=_("آدرس سایت"), max_length=200)
    computer_logo = models.ImageField(verbose_name=_("لوگوی سایت برای کامپیوتر"), upload_to='images/logos/', help_text=_("72 * 394"))
    mobile_logo = models.ImageField(verbose_name=_("لوگوی سایت برای موبایل"), upload_to='images/logos/', help_text=_("56 * 202"))
    copy_right = models.CharField(verbose_name=_("متن کپی رایت"), max_length=250)
    

    class Meta:
        verbose_name = _("تظیم")
        verbose_name_plural = _("تنظیمات")

    def __str__(self):
        return self.site_name


class SocialNetwork(models.Model):
    setting = models.ForeignKey(Setting, verbose_name=_("تظیم"), on_delete=models.DO_NOTHING, related_name='socials')
    name = models.CharField(verbose_name=_("نام شبکه"), max_length=50)
    url = models.URLField(verbose_name=_("لینک"), max_length=200)
    

    class Meta:
        verbose_name = _("شبکه مجازی")
        verbose_name_plural = _("شبکه های مجازی")

    def __str__(self):
        return self.name
    