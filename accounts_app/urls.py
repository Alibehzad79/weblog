from django.urls import path
from accounts_app.views import ( login_view,
                                logout_view,
                                sign_up_view,
                                forget_passowrd,
                                password_reset_done,
                                reset_password,
                                password_reset_complete,
                                # admin_index,
)

app_name="accounts"
urlpatterns = [
    path('login/', login_view, name='login'),
    path('sign-up/', sign_up_view, name='sign_up'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', forget_passowrd, name='forget_password'),
    path('password-reset/done/', password_reset_done, name='forget_password_done'),
    path('password-reset-confirm/<str:email_reset_hash>/', reset_password, name='reset_password'),
    path('password-reset-complete/', password_reset_complete, name='password_reset_complete'),
    # path('admin/index/', admin_index, name="admin_index"),
]
