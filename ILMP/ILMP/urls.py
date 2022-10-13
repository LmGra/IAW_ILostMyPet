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
from django.urls import path
from ILMP_app import views
from ILMP_app.views import MascotasListView, EncuentrosListView, PerdidosListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', MascotasListView.as_view()),
    path('encuentros/', EncuentrosListView.as_view()),
    path('perdidos/', PerdidosListView.as_view()),
]
