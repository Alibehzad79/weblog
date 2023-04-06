from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SearchAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search_app'
    verbose_name = _("بخش سرچ")