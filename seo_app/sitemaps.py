from django.contrib.sitemaps import Sitemap
from blog_app.models import ArticleModel
from about_app.models import AboutModel

class ArticleModelSitemap(Sitemap):
    def items(self):
        return ArticleModel.objects.filter(status=ArticleModel.Status.published).all()
        
    def lastmod(self, obj):
        return obj.date_updated