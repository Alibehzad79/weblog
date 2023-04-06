from django.contrib import admin
from category_app.models import CategoryModel
# Register your models here.

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('date_created',)
    search_fields = ('name', 'slug')