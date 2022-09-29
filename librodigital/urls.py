"""librodigital URL Configuration

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
from libro import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.exit, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('afiliados/', views.afiliados, name='afiliados'),
    path('afiliados/crear/', views.afiliado_create, name='afiliado_create'),
    path('afiliados/<int:afiliado_id>/', views.afiliado_detail, name='afiliado_detail'),
    path('afiliados/<int:afiliado_id>/completed', views.afiliado_completed, name='afiliado_completed'),
    path('afiliados/<int:afiliado_id>/delete', views.afiliado_delete, name='afiliado_delete'),
    path('afiliados_completed/', views.afiliados_completed, name='afiliados_completed'),

]
