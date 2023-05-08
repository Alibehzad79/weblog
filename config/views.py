from django.shortcuts import render
from site_settings_app.models import Setting

def error_404(request, exception):
    template_name = 'base/error_404.html'
    setting = Setting.objects.last()
    context = {
        'setting': setting,
    }
    return render(request, template_name, context)