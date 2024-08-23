
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('home',views.home,name="home"),
    path('resetpwd',views.resetpwd,name="resetpwd"),
    path('updatepwd',views.updatepwd,name="updatepwd"),

    path('addaitems',views.addaitems,name="addaitems"),
    path('adda_list',views.adda_list,name="adda_list"),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/', views.view_cart, name="view_cart"),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('adda_update_quantity/<int:item_id>/<str:action>/', views.adda_update_quantity,name='adda_update_quantity'),
    path('search',views.search,name="search"),


    path('naturalsitems', views.naturalsitems, name="naturalsitems"),
    path('naturals_list', views.naturals_list, name="naturals_list"),
    path('naturals_add_to_cart/<int:item_id>/', views.naturals_add_to_cart, name="naturals_add_to_cart"),
    path('naturals_cart/', views.naturals_view_cart, name="naturals_view_cart"),
    path('naturals_remove_from_cart/<int:item_id>/', views.naturals_remove_from_cart, name="naturals_remove_from_cart"),
    path('update_quantity/<int:item_id>/<str:action>/', views.naturals_update_quantity, name='naturals_update_quantity'),
    path('nsearch',views.nsearch,name="nsearch"),

    path('rasitems',views.rasitems,name="rasitems"),
    path('ras_list',views.ras_list,name="ras_list"),
    path('ras_add_to_cart/<int:item_id>/', views.ras_add_to_cart, name="ras_add_to_cart"),
    path('rcart/', views.ras_view_cart, name="ras_view_cart"),
    path('ras_remove_from_cart/<int:item_id>/', views.ras_remove_from_cart, name="ras_remove_from_cart"),
    path('ras_update_quantity/<int:item_id>/<str:action>/', views.ras_update_quantity,name='ras_update_quantity'),
    path('rsearch',views.rsearch,name="rsearch"),

    path('usitems',views.usitems,name="usitems"),
    path('us_list',views.us_list,name="us_list"),
    path('us_add_to_cart/<int:item_id>/', views.us_add_to_cart, name="us_add_to_cart"),
    path('ucart/', views.us_view_cart, name="us_view_cart"),
    path('us_remove_from_cart/<int:item_id>/', views.us_remove_from_cart, name="us_remove_from_cart"),
    path('us_update_quantity/<int:item_id>/<str:action>/', views.us_update_quantity,name='us_update_quantity'),
    path('usearch',views.usearch,name="usearch"),

]