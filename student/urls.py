
from django.urls import path

from . import views

urlpatterns=[
    path('',views.login,name="login"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('home',views.home,name="home"),

    path('addaitems',views.addaitems,name="addaitems"),
    path('adda_list',views.adda_list,name="adda_list"),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/', views.view_cart, name="view_cart"),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('adda_update_quantity/<int:item_id>/<str:action>/', views.adda_update_quantity,name='adda_update_quantity'),
    path('naturalsitems', views.naturalsitems, name="naturalsitems"),
    path('naturals_list', views.naturals_list, name="naturals_list"),
    path('naturals_add_to_cart/<int:item_id>/', views.naturals_add_to_cart, name="naturals_add_to_cart"),
    path('naturals_cart/', views.naturals_view_cart, name="naturals_view_cart"),
    path('naturals_remove_from_cart/<int:item_id>/', views.naturals_remove_from_cart, name="naturals_remove_from_cart"),

    path('update_quantity/<int:item_id>/<str:action>/', views.naturals_update_quantity, name='naturals_update_quantity'),
]