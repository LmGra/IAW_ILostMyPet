from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from ILMP_app.forms import ContactForm
from ILMP_app.models import Mascotas, Encuentros, Perdidos

#Página de inicio

def index(request):
    return render(request, "ILMP_app/index.html")

#Mascotas

class MascotasListView(ListView):
    model = Mascotas

class MascotasDetailView(DetailView):
    model = Mascotas

#Encontradas

class EncuentrosListView(ListView):
    model = Encuentros

class EncuentrosDetailView(DetailView):
    model = Encuentros

#Buscadas

class PerdidosListView(ListView):
    model = Perdidos

class PerdidosDetailView(DetailView):
    model = Perdidos

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

#def index(request):
#    return render(request,'ILMP_app/index.html')

# Create your views here.
