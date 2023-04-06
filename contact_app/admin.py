from django.contrib import admin
from contact_app.models import ContactModel, ContactModelForm

# Register your models here.
@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_dispaly = ('title',)

@admin.register(ContactModelForm)
class ContactModelFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'date_sent')
    search_field = ('name', 'email', 'subject', 'text')

