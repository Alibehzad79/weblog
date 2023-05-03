from django.urls import path
from accounts_app.views import login_view, logout_view, sign_up_view
app_name="accounts"
urlpatterns = [
    path('login/', login_view, name='login'),
    path('sign-up/', sign_up_view, name='sign_up'),
    path('logout/', logout_view, name='logout'),
]
