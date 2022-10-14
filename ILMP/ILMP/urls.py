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
from ILMP_app.views import PerdidosDetailView, EncuentrosDetailView, MascotasDetailView, MascotasListView, EncuentrosListView, PerdidosListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', MascotasListView.as_view()),
    path('mascotas/<int:pk>/', MascotasDetailView.as_view(), name='mascotas-detail'),
    path('encuentros/', EncuentrosListView.as_view()),
    path('encuentros/<int:pk>/', EncuentrosDetailView.as_view(), name='encuentros-detail'),
    path('perdidos/', PerdidosListView.as_view()),
    path('perdidos/<int:pk>/', PerdidosDetailView.as_view(), name='perdidos-detail'),
]
