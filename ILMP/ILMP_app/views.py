from django.shortcuts import render

from django.views.generic import ListView
from ILMP_app.models import Mascotas, Encuentros, Perdidos

class MascotasListView(ListView):
    model = Mascotas

class EncuentrosListView(ListView):
    model = Encuentros

class PerdidosListView(ListView):
    model = Perdidos

#def index(request):
#    return render(request,'ILMP_app/index.html')

# Create your views here.
