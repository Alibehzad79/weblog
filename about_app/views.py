from django.shortcuts import render
from about_app.models import AboutModel
from django.http import HttpResponseNotFound
# Create your views here.

def about_page(request):
    template_name = 'about/about.html'
    try:
        about = AboutModel.objects.last()
    except:
        about = None
    context = {
        'about': about,
    }
    return render(request, template_name, context)