from django.contrib.sitemaps import Sitemap
from blog_app.models import ArticleModel
from about_app.models import AboutModel
from contact_app.models import ContactModel
from category_app.models import CategoryModel
class ArticleModelSitemap(Sitemap):
    def items(self):
        return ArticleModel.objects.filter(status=ArticleModel.Status.published).all()
        
    def lastmod(self, obj):
        return obj.date_updated

class AboutModelSitemap(Sitemap):
    def items(self):
        return AboutModel.objects.all()
        
    def lastmod(self, obj):
        return obj.date_created    
    
class ContactModelSitemap(Sitemap):
    def items(self):
        return ContactModel.objects.all()
        
    def lastmod(self, obj):
        return obj.date_created             