from django.urls import path
from about_app.views import about_page
app_name='about'
urlpatterns = [
    path('', about_page, name='about')
]
