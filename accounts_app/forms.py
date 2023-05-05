from django import forms
from django.core import validators
from accounts_app.models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder":"ایمیل خود را وارد کنید"}),
        required=True,
        label="ایمیل",
        validators = [
            validators.EmailValidator('لطفا ایمیل معتبر وارد کنید')
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"رمز خود را وارد کنید"}),
        required=True,
        label="رمز عبور"
    )
    
    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"id":"fruit1", "name":"keep-log", "checked":"checked"}),
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('رمز عبور یا نام کاربری اشتباه است')
        return email

class SignUpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder":"ایمیل معتبر وارد کنید"}),
        label="ایمیل",
        validators=[
            validators.EmailValidator("لطفا ایمیل معتبر وارد کنید"),
        ],
        required=True,
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"رمز عبور خود را وارد کنید"}),
        label="رمز عبور",
        max_length=12,
        min_length=8,
        required=True,
        validators = [
            validators.MinLengthValidator(6, 'حداقل حروف، 6 حرف هست'),
            validators.MaxLengthValidator(12, 'حداکثر حروف، 12 حرف هست'),
        ],
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"رمز عبور خود را تائید کنید"}),
        label="تائید رمز عبور",
        max_length=12,
        min_length=8,
        required=True,
        validators = [
            validators.MinLengthValidator(6, 'حداقل حروف، 6 حرف هست'),
            validators.MaxLengthValidator(12, 'حداکثر حروف، 12 حرف هست'),
        ],
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("کاربری قبلا با این ایمیل ثبت نام کرده")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('رمز عبور ها یکسان نیست')
        return password1
    
    

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"ایمیل خود را وارد کنید"}), required=True, label="ایمیل")
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('کاربری با این ایمیل یافت نشد')
        return email


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':"رمز عبور جدید را وارد کنید"}),
        max_length=12,
        min_length=8,
        required=True,
        label="رمز عبور جدید",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':"رمز عبور جدید را تایید کنید"}),
        max_length=12,
        min_length=8,
        required=True,
        label="تایید رمز عبور جدید",
    )
    
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise form.ValidationError('رمز عبور ها یکسان نیست')
        return password1