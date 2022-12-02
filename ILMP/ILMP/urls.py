"""ILMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ILMP_app import views
from ILMP_app.views import index, UserDeleteView, UserUpdateView, UserCreateView, UserDetailView, UserListView, EncuentrosDeleteView, EncuentrosUpdateView, EncuentrosCreateView, PerdidosUpdateView, PerdidosDeleteView, PerdidosCreateView ,MascotasDeleteView, MascotasUpdateView, MascotasCreateView, PerdidosDetailView, EncuentrosDetailView, MascotasDetailView, MascotasListView, EncuentrosListView, PerdidosListView
from django.views.generic.base import TemplateView
from ILMP_app.api import router
##Api

#from django.urls import path, include
#from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets


##

urlpatterns = [
    
    #Index
    #path('', index),
    path('', include(('ILMP_app.urls','ilmp'),namespace="ilmp")),

    #Admin
    path('admin/', admin.site.urls),

    #Accounts
    #path("accounts/", ("django.contrib.auth.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register_request, name="register"),
    #path("", TemplateView.as_view(template_name="ILMP_app/index.html"),name="index"),
    
    #Api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
