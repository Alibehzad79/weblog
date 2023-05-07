from django.shortcuts import redirect, render
from category_app.models import CategoryModel
from blog_app.models import ArticleModel
from subscribe_app.forms import SubscribeForm
from subscribe_app.models import Subscribe
from datetime import datetime
from django.contrib import messages
from site_settings_app.models import Setting
from seo_app.models import HomePageSeo
from ads_app.models import HomePageAds
# Create your views here.

def base(request):
    template_name = 'base/base.html'
    seo = HomePageSeo.objects.last()
    settings = Setting.objects.last()
    if request.method == 'POST':
        form = SubscribeForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            new_sub = Subscribe.objects.create(email=email, date_joined=datetime.now(), status=Subscribe.Status.subscribe)
            if new_sub is not None:
                messages.add_message(request, messages.SUCCESS, "با موفقیت عضو شدید")
                return redirect('base')
    else:
        form = SubscribeForm()
    ads = HomePageAds.objects.last()
    context = {
        'form':form,
        'seo': seo,
        'settings': settings,
        'ads': ads,
    }
    return render(request, template_name, context)

def header(request):
    template_name = 'base/header.html'
    categories = CategoryModel.objects.all()
    setting = Setting.objects.last()
    context = {
        'categories': categories,
        'setting': setting,
    }
    return render(request, template_name, context)

def loader(request):
    template_name = 'base/loader.html'
    settings = Setting.objects.last()
    context = {
        'settings': settings,
    }
    return render(request, template_name, context)

def fovicon(request):
    template_name = 'base/fovicon.html'
    settings = Setting.objects.last()
    context = {
        'settings': settings,
    }
    return render(request, template_name, context)


def footer(request):
    template_name = 'base/footer.html'
    categories = CategoryModel.objects.all()
    setting = Setting.objects.last()
    context = {
        'categories': categories,
        'setting': setting,
    }
    return render(request, template_name, context)

def banner_news(request):
    template_name = 'home/banner_news.html'
    trending_posts = ArticleModel.objects.order_by('-date_updated').all()[:8]
    context = {
        'trending_posts': trending_posts,
    }
    return render(request, template_name, context)


def latest_posts(request):
    template_name = 'home/latest_posts.html'
    latest_posts = ArticleModel.objects.order_by('-date_created').all()[:5]
    context = {
        'latest_posts': latest_posts,
    }
    return render(request, template_name, context)

def top_posts(request):
    template_name = 'home/top_posts.html'
    top_posts = ArticleModel.objects.order_by('-impression_count').all()[:5]
    context = {
        'top_posts':top_posts,
    }
    return render(request, template_name, context)

def popular_posts(request):
    template_name = 'home/popular_posts.html'
    popular_posts = ArticleModel.objects.order_by('-reach_count').all()[:3]
    context = {
        'popular_posts': popular_posts,
    }
    return render(request, template_name, context)

def sliders(request):
    template_name = 'home/sliders.html'
    categoris = CategoryModel.objects.all()
    context = {
        'categoris': categoris,
    }
    return render(request, template_name, context)