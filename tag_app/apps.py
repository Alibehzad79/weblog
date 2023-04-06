from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TagAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tag_app'
    verbose_name = _("بخش تگ ها")