from django.urls import path
from contact_app.views import contact_page
app_name='contact'
urlpatterns = [
    path('', contact_page, name='contact')
]
