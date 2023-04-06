from django.contrib import admin
from tag_app.models import TagModel
# Register your models here.

@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('date_created',)
    search_fields = ('name', 'slug')