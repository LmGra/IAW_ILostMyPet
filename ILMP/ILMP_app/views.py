from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from ILMP_app.models import Mascotas, Encuentros, Perdidos

class MascotasListView(ListView):
    model = Mascotas

class MascotasDetailView(DetailView):

    model = Mascotas

    #context_object_name = 'mascotas'
    #queryset = Mascotas.objects.all()


class EncuentrosListView(ListView):
    model = Encuentros

class EncuentrosDetailView(DetailView):

    model = Encuentros

class PerdidosListView(ListView):
    model = Perdidos

class PerdidosDetailView(DetailView):

    model = Perdidos

#def index(request):
#    return render(request,'ILMP_app/index.html')

# Create your views here.
