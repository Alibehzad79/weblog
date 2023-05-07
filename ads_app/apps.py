from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AdsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ads_app'
    verbose_name=_('بخش تبلیغات')