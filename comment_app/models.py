from django.db import models
from django.utils.translation import gettext_lazy as _
from blog_app.models import ArticleModel
# Create your models here.

class Comment(models.Model):
    class Status(models.TextChoices):
        read = 'read', _('خوانده شده')
        unread = 'unread', _('خوانده نشده')
    
    article = models.ForeignKey(ArticleModel, verbose_name=_("مقاله"), on_delete=models.DO_NOTHING, related_name='comments')
    name = models.CharField(max_length=20, verbose_name=_('نام'))
    email = models.EmailField(verbose_name=_('ایمیل'), help_text=_('example@test.com'))
    website = models.URLField(help_text=_('https:// | میتواند خالی بماند'), blank=True, null=True, verbose_name=_('سایت'))
    comment = models.TextField(verbose_name=_('کامنت'))
    date_sent = models.DateTimeField(auto_now_add=False, verbose_name=_('تاریخ ارسال'))
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.unread, verbose_name=_('وضعیت'))
    
    
    class Meta:
        verbose_name = _('کامنت')
        verbose_name_plural = _('کامنت ها')
        ordering = ['-date_sent']
    
    def __str__(self):
        return self.email