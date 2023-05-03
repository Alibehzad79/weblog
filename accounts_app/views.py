from django.shortcuts import render, redirect
from accounts_app.forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate, logout
from accounts_app.models import CustomUser
from django.contrib.auth.hashers import make_password
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
# TODO ForgetPasswrod
