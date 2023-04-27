from django.contrib import admin
from site_settings_app.models import Setting, SocialNetwork

# Register your models here.

class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_address')
    search_field = ('site_name', 'site_address')
    inlines = [SocialNetworkInline]