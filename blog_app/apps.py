from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'
    verbose_name = _("بخش وبلاگ")