from django.shortcuts import render

from django.views.generic import ListView
from ILMP_app.models import Mascotas

class MascotasListView(ListView):
    model = Mascotas

#def index(request):
#    return render(request,'ILMP_app/index.html')

# Create your views here.
