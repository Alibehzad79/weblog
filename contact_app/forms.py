from django import forms
from contact_app.models import ContactModelForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModelForm
        exclude = ['date_sent', 'answre', 'status']
