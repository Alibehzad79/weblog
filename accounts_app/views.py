from django.shortcuts import render, redirect
from accounts_app.forms import LoginForm, SignUpForm, ForgetPasswordForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from accounts_app.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from site_settings_app.models import Setting
from config import settings
# Create your views here.
def login_view(request):
    template_name = 'accounts/login.html'
    if request.user.is_authenticated:
        return redirect('base')
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            email = email.lower()
            password = form.cleaned_data.get('password')
            remmeber_me = form.cleaned_data.get('remember_me')
            username = CustomUser.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if remmeber_me:
                    request.session.set_expiry(1209600)
                else:
                    request.session.set_expiry(0)
                return redirect('base')
    else:
        form = LoginForm()    
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def sign_up_view(request):
    template_name = 'accounts/sign_up.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            email = email.lower()
            password1 = form.cleaned_data.get('password1')
            password1 = make_password(password1)
            new_user = CustomUser.objects.create(username=email, email=email, password=password1)
            if new_user is not None:
                new_user.save()
                return redirect('accounts:login')
    else:
        form = SignUpForm()    
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def forget_passowrd(request):
    if request.user.is_authenticated:
        return redirect('base')
    template_name = 'accounts/password_reset_form.html'
    setting = Setting.objects.last()
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            email = email.lower()
            user = CustomUser.objects.get(email=email)
            user.forget_password_hash = get_random_string(64)
            user.save()
            sendEmail = send_mail(
               "Password Reset",
                f"{setting.site_address}accounts/password-reset-confirm/{user.forget_password_hash}/",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
            if sendEmail:
                return redirect('accounts:forget_password_done')
    else:
        form = ForgetPasswordForm() 
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def password_reset_done(request):
    if request.user.is_authenticated:
        return redirect('base')
    template_name = 'accounts/password_reset_done.html'
    context = {
        'message': 'ایمیل بازیابی رمز عبور با موفقیت ارسال شد',
    }
    return render(request, template_name, context)

def reset_password(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('base')
    template_name = 'accounts/password_reset_confirm.html'
    email_reset_hash = kwargs['email_reset_hash']
    if request.method == 'POST':
        form = PasswordResetForm(request.POST or None)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            user = CustomUser.objects.get(forget_password_hash=email_reset_hash)
            user.set_password(password1)
            user.forget_password_hash = ''
            user.save()
            return redirect('accounts:password_reset_complete')
    else:
        form = PasswordResetForm()
    
    context = {
        'form':form,
    }   
    return render(request, template_name, context) 

def password_reset_complete(request):
    if request.user.is_authenticated:
        return redirect('base')
    template_name = 'accounts/password_reset_complete.html'
    context = {
        'message':'رمز عبور با موفقیت تغییر یافت',
    }  
    return render(request, template_name, context) 