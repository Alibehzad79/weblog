from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CommentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comment_app'
    verbose_name = _("بخش کامنت ها")
