from django.urls import path , include
from . import views
from login.image import Captcha_Simple
urlpatterns = [
    path('login/', views.login,name='login'),
    path('login_check1/' , Captcha_Simple.login_check, name="login_check1"),
    path('login/refresh/' , views.refresh , name="refresh"),
    path('img_captcha/' , Captcha_Simple.img_captcha , name="img_captcha")
]