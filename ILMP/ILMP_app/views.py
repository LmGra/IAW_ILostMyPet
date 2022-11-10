from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from ILMP_app.forms import ContactForm
from ILMP_app.models import User ,Mascotas, Encuentros, Perdidos
from django.urls import reverse_lazy
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
#Página de inicio

def index(request):
    return render(request, "ILMP_app/index.html")


#Usuarios

class UserListView(ListView):
    model = User

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('index')

class UserUpdateView(UpdateView):
    model = User
    fields = ['genderUsr', 'birthUsr', 'telUsr', 'imgUsr', 'ubiUsr']
    template_name_sufix = '_update_form'

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('index')

#Mascotas

class MascotasListView(ListView):
    model = Mascotas

class MascotasDetailView(DetailView):
    model = Mascotas

class MascotasCreateView(CreateView):
    model = Mascotas
    fields = ['namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet', 'usrPet']
    success_url = reverse_lazy('mascotas-list')

class MascotasUpdateView(UpdateView):
    model = Mascotas
    fields = ['namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet', 'usrPet']
    template_name_sufix = '_update_form'

class MascotasDeleteView(DeleteView):
    model = Mascotas
    success_url = reverse_lazy('mascotas-list')

#Encontradas

class EncuentrosListView(ListView):
    model = Encuentros

class EncuentrosDetailView(DetailView):
    model = Encuentros

class EncuentrosCreateView(CreateView):
    model = Encuentros
    fields = ['typeFind', 'infoFind', 'genderFind', 'ubiFind']
    success_url = reverse_lazy('encuentros-list')

class EncuentrosUpdateView(UpdateView):
    model = Encuentros
    fields = ['typeFind', 'infoFind', 'genderFind', 'ubiFind']
    template_name_sufix = '_update_form'

class EncuentrosDeleteView(DeleteView):
    model = Encuentros
    success_url = reverse_lazy('encuentros-list')

#Buscadas

class PerdidosListView(ListView):
    model = Perdidos

class PerdidosDetailView(DetailView):
    model = Perdidos

class PerdidosCreateView(CreateView):
    model = Perdidos
    fields = ['infoLost', 'dateLost', 'petLost', 'ubiLost']
    #success_url = reverse_lazy('perdidos-list')

class PerdidosUpdateView(UpdateView):
    model = Perdidos
    fields = ['infoLost', 'dateLost', 'petLost', 'ubiLost']
    template_name_sufix = '_update_form'

class PerdidosDeleteView(DeleteView):
    model = Perdidos
    success_url = reverse_lazy('perdidos-list')


#def index(request):
#    return render(request,'ILMP_app/index.html')

# Create your views here.



