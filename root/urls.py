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
]
