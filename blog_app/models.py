from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from category_app.models import CategoryModel
from tag_app.models import TagModel
# ckeditor fields
from ckeditor.fields import RichTextField
from django.db.models import Q
# Create your models here.

class ArticleManager(models.Manager):
    def get_search(self, query, status):
        lookup = (
            Q(title__icontains=query)|
            Q(author__username__icontains=query)|
            Q(author__first_name__icontains=query)|
            Q(author__last_name__icontains=query)|
            Q(slug__icontains=query)|
            Q(content__icontains=query)|
            Q(category__name__icontains=query)|
            Q(category__slug__icontains=query)|
            Q(tags__name__icontains=query)|
            Q(tags__slug__icontains=query)
        )
        
        return self.get_queryset().filter(lookup, status=status).all().distinct()

class ArticleModel(models.Model):
    class Status(models.TextChoices):
        published = 'published', _('منتشر شده')
        unpublished = 'unpublished', _('منتشر نشده')
    author = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, verbose_name=_('نویسنده'))
    title = models.CharField(max_length=160, verbose_name=_(
        'عنوان'), help_text=_('160 کاراکتر'))
    slug = models.SlugField(max_length=160, help_text=_(
        'مثال: article-name'), verbose_name=_('اسلاگ'), unique=True)
    content = RichTextField(verbose_name=_('محتوا'))
    image = models.ImageField(
        upload_to='images/articles/', verbose_name=_('تصویر'))
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING,
                                 related_name='categories', verbose_name=_('دسته بندی'))

    tags = models.ManyToManyField(TagModel, verbose_name=_('تگ ها'))
    reach_count = models.IntegerField(
        default=0, verbose_name=_('تعداد ریچ پست'))
    impression_count = models.IntegerField(
        default=0, verbose_name=_('تعداد ایمرشن پست'))
    date_created = models.DateTimeField(
        auto_now_add=False, verbose_name=_('تاریخ ایجاد'))
    date_updated = models.DateTimeField(
        auto_now_add=False, verbose_name=_('تاریخ آپدیت'))

    status = models.CharField(max_length=20, choices=Status.choices,
                              default=Status.unpublished, verbose_name=_('وضعیت'))

    
    objects = ArticleManager()
    class Meta:
        verbose_name = _('مقاله')
        verbose_name_plural = _('مقاله ها')
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"pk": self.pk, "slug": self.slug})
    
    # def get_image(self): # config image width & heigth
        # pass