from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ContactAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_app'
    verbose_name = _("بخش تماس با ما")