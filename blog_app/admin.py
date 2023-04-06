from django.contrib import admin
from blog_app.models import ArticleModel
# Register your models here.


@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'reach_count', 'impression_count', 'date_created', 'status', 'category')
    list_editable = ('status', 'category')
    list_filter = ('category', 'tags', 'status', 'date_created', 'date_updated')
    search_fields = ('title', 'content', 'author', 'category', 'tags')