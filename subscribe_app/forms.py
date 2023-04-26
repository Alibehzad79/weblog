from django import forms
from subscribe_app.models import Subscribe

class SubscribeForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "ایمیل خود را وارد کنید"}), required=True, max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Subscribe.objects.filter(email=email).exists():
            raise forms.ValidationError('شما قبلا عضو شده اید.')
        return email.lower()
    
