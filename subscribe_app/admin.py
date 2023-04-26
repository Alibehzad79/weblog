from django.contrib import admin
from subscribe_app.models import Subscribe
# Register your models here.

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'status')
    list_filter = ('date_joined','status')
    list_editable = ('status',)
    search_fields = ('email',)

