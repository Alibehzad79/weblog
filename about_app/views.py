from django.shortcuts import render
from about_app.models import AboutModel
from ads_app.models import AboutPageAds
# Create your views here.

def about_page(request):
    template_name = 'about/about.html'
    try:
        about = AboutModel.objects.last()
    except:
        about = None
    ads = AboutPageAds.objects.last()
    context = {
        'about': about,
        'ads': ads,
    }
    return render(request, template_name, context)