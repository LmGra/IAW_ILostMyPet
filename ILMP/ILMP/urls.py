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
from ILMP_app.views import index, EncuentrosDeleteView, EncuentrosUpdateView, EncuentrosCreateView, PerdidosUpdateView, PerdidosDeleteView, PerdidosCreateView ,MascotasDeleteView, MascotasUpdateView, MascotasCreateView, PerdidosDetailView, EncuentrosDetailView, MascotasDetailView, MascotasListView, EncuentrosListView, PerdidosListView
from django.views.generic.base import TemplateView

urlpatterns = [
    #Index
    #path('', index),

    #Admin
    path('admin/', admin.site.urls),

    #Accounts
    #path("accounts/", ("django.contrib.auth.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="ILMP_app/index.html"),name="index"),
    

    #Mascotas
    path('mascotas/', MascotasListView.as_view(), name='mascotas-list'),
    path('mascotas/<int:pk>/', MascotasDetailView.as_view(), name='mascotas-detail'),
    path("mascotas/add/", MascotasCreateView.as_view(), name='mascotas-add'),
    path('mascotas/<int:pk>/edit/', MascotasUpdateView.as_view(), name='mascotas-update'),
    path('mascotas/<int:pk>/delete/', MascotasDeleteView.as_view(), name='mascotas-delete'),

    #Encuentros
    path('encuentros/', EncuentrosListView.as_view()),
    path('encuentros/<int:pk>/', EncuentrosDetailView.as_view(), name='encuentros-detail'),
    path("encuentros/add/", EncuentrosCreateView.as_view(), name='encuentros-add'),
    path('encuentros/<int:pk>/edit/', EncuentrosUpdateView.as_view(), name='encuentros-update'),
    path('encuentros/<int:pk>/delete/', EncuentrosDeleteView.as_view(), name='encuentros-delete'),

    #Perdidos
    path('perdidos/', PerdidosListView.as_view()),
    path('perdidos/<int:pk>/', PerdidosDetailView.as_view(), name='perdidos-detail'),
    path("perdidos/add/", PerdidosCreateView.as_view(), name='perdidos-add'),
    path('perdidos/<int:pk>/edit/', PerdidosUpdateView.as_view(), name='perdidos-update'),
    path('perdidos/<int:pk>/delete/', PerdidosDeleteView.as_view(), name='perdidos-delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
