from django.urls import path , include
from . import views
urlpatterns = [
    path('login/', views.login,name='login'),
    path('login_check/' , views.login_check, name="login_check"),
    # path(r'^captcha/' , include('captcha.urls')),
    path('login/refresh/' , views.refresh , name="refresh"),
    path('img_captcha/' , views.img_captcha , name="img_captcha"),
    # path('refresh_captcha/' , views.refresh_captcha , name="refresh_captcha")
]