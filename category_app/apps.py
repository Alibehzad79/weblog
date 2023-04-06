from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CategoryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category_app'
    verbose_name = _("بخش دسته بندی ها")