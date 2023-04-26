from django.urls import path
from home_app.views import home
app_name='index'
urlpatterns = [
    path('index/', home, name='index')
]
