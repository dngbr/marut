"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('despre/', views.about, name="about"),
    path('servicii/', views.services, name="services"),
    path('produse/', views.products, name="products"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('ferestre/', views.ferestre, name="ferestre"),
    path('usi/', views.usi, name="usi"),
    path('rulouri/', views.rulouri, name="rulouri"),
    path('accesorii/', views.accesorii, name="accesorii"),
    path('aluplast/', views.aluplast, name="aluplast"),
    path('euro/', views.euro, name="euro"),
    path('synego/', views.synego, name="synego"),
    path('geneo/', views.geneo, name="geneo"),
    path('articol1/', views.articol1, name='articol1'),
    path('articol2/', views.articol2, name='articol2'),
    path('articol3/', views.articol3, name='articol3'),
    path('articol4/', views.articol4, name='articol4'),
    path('articol5/', views.articol5, name='articol5'),
    path('articol6/', views.articol6, name='articol6'),
    path('articol7/', views.articol7, name='articol7'),
    path('articol8/', views.articol8, name='articol8'),
    path('articol9/', views.articol9, name='articol9'),
    path('articol10/', views.articol10, name='articol10'),
]
