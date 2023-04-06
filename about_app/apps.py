from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AboutAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_app'
    verbose_name = _("بخش درباره ما")
