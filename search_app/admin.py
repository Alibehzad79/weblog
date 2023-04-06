from django.contrib import admin
from search_app.models import Search
# Register your models here.


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('query_name', 'search_count',
                    'date_created', 'date_updated')
    list_filter = ('date_created', 'date_updated', 'search_count')
    search_fields = ('query_name',)
