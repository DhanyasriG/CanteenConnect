from django.urls import path

from . import views


urlpatterns=[
    path('restaurant/rlogin',views.rlogin,name="rlogin"),
    path('restaurant/rchecklogin', views.rchecklogin, name="rchecklogin"),
    path('restaurant/rhome', views.rhome, name="rhome"),

    path('restaurant/adda', views.adda, name="adda"),
    path('restaurant/addaupdate/<int:id>/', views.addaupdate, name='addaupdate'),
    path('restaurant/search', views.search, name="search"),

    path('restaurant/ras', views.ras, name="ras"),
    path('restaurant/rasupdate/<int:id>/', views.rasupdate, name='rasupdate'),
    path('restaurant/rassearch', views.rassearch, name="rassearch"),

    path('restaurant/us', views.us, name="us"),
    path('restaurant/usupdate/<int:id>/', views.usupdate, name='usupdate'),
    path('restaurant/ussearch', views.ussearch, name="ussearch"),

    path('restaurant/naturals', views.naturals, name="naturals"),
    path('restaurant/naturalsupdate/<int:id>/', views.naturalsupdate, name='naturalsupdate'),
    path('restaurant/nsearch', views.nsearch, name="nsearch"),

]