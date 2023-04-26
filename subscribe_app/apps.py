from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SubscribeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscribe_app'
    verbose_name = _('بخش سابسکرایب')