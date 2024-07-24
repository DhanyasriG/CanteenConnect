
from django.urls import path

from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('home',views.home,name="home"),
]