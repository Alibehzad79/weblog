from django.db import models
from django.utils.translation import gettext_lazy as _
from blog_app.models import ArticleModel
from django.utils import html
# Create your models here.


class ArticlesSEO(models.Model):
    article = models.ForeignKey(
        ArticleModel, on_delete=models.DO_NOTHING, verbose_name=_("مقاله"), related_name=_("article_seo"))
    subject = models.CharField(max_length=50, verbose_name=_(
        "عنوان"), help_text=_("حداکثر 50 کاراکتر"))
    keywords = models.TextField(verbose_name=_("کلمات کلیدی"), help_text=_(
        "جدا سازی با کامای انگلیسی - مثال: مقاله, مقاله۲"), blank=True)
    description = models.CharField(max_length=160, verbose_name=_(
        "توضیحات"), help_text=_("حداکثر 160 کاراکتر"))
    author_name = models.CharField(max_length=50, verbose_name=_(
        "نام نویسنده"), help_text=_("حداکثر 50 کاراکتر"))
    refresh = models.CharField(blank=True, null=True, max_length=150, verbose_name=_(
        "Refresh"), help_text=_("الزامی نیست"))

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = _("سئو")
        verbose_name_plural = _("سئوی مقاله ها")

    def get_subject(self):
        if self.subject is not '':
            return html.format_html(f'<meta name="subject" content="{self.subject}">')
        else:
            return html.format_html(f'<meta name="subject" content="{self.article.title}">')

    def get_description(self):
        if self.description is not '':
            return html.format_html(f'<meta name="description" content="{self.description}">')
        else:
            return html.format_html(f'<meta name="description" content="{self.description}">')

    def get_viewport(self):
        return html.format_html(f'<meta name="viewport" content="width=device-width, initial-scale=1.0">')

    def get_charset(self):
        return html.format_html(f'<meta charset="UTF-8">')

    def get_refresh(self):
        if self.refresh is not '':
            return html.format_html(f'<meta http-equiv="refresh" content="{self.refresh}">')
        else:
            return None

    def get_keywords(self):
        if self.keywords is not '':
            return html.format_html(f'<meta name="keywords" content="{self.keywords}">')
        else:
            return html.format_html(f'<meta name="keywords" content="{self.article.category.name}, {self.article.category.slug}">')

    def get_author(self):
        if self.author_name is not '':
            return html.format_html(f'<meta name="author" content="{self.author_name}">')
        else:
            return html.format_html(f'<meta name="author" content="{self.article.author.get_username}">')

class HomePageSeo(models.Model):
    keywords = models.TextField(verbose_name=_("کلمات کلیدی"), help_text=_(
        "جدا سازی با کامای انگلیسی - مثال: مقاله, مقاله۲"), blank=True)
    description = models.CharField(max_length=160, verbose_name=_(
        "توضیحات"), help_text=_("حداکثر 160 کاراکتر"))
    

    class Meta:
        verbose_name = _("صفحه ی خانه")
        verbose_name_plural = _("صفحه ی خانه")

    def __str__(self):
        return self.keywords

    def get_keywords(self):
        if self.keywords is not '':
            return html.format_html(f'<meta name="keywords" content="{self.keywords}">')
    def get_description(self):
        if self.description is not '':
            return html.format_html(f'<meta name="description" content="{self.description}">')

class ArticleListSeo(models.Model):
    keywords = models.TextField(verbose_name=_("کلمات کلیدی"), help_text=_(
        "جدا سازی با کامای انگلیسی - مثال: مقاله, مقاله۲"), blank=True)
    description = models.CharField(max_length=160, verbose_name=_(
        "توضیحات"), help_text=_("حداکثر 160 کاراکتر"))
    

    class Meta:
        verbose_name = _("صفحه لیست مقاله ها")
        verbose_name_plural = _("صفحه لیست مقاله ها")

    def __str__(self):
        return self.keywords

    def get_keywords(self):
        if self.keywords is not '':
            return html.format_html(f'<meta name="keywords" content="{self.keywords}">')
    def get_description(self):
        if self.description is not '':
            return html.format_html(f'<meta name="description" content="{self.description}">')