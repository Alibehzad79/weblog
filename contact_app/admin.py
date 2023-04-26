from django.contrib import admin
from contact_app.models import ContactModel, ContactModelForm, Telephone, Email, Address

class TelephoneInline(admin.TabularInline):
    model = Telephone

class EmailInline(admin.TabularInline):
    model = Email

class AddressInline(admin.TabularInline):
    model = Address
    

# Register your models here.
@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_dispaly = ('title',)
    inlines = [TelephoneInline, EmailInline, AddressInline]

@admin.register(ContactModelForm)
class ContactModelFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'date_sent')
    search_field = ('name', 'email', 'subject', 'text')
    