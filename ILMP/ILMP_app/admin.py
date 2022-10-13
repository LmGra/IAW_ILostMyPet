from django.contrib import admin

from .models import Mascotas
from .models import Perdidos
from .models import Encuentros
#from .models import Area
from .models import Usuarios

admin.site.register(Mascotas)
admin.site.register(Perdidos)
admin.site.register(Encuentros)
#admin.site.register(Area)
admin.site.register(Usuarios)

# Register your models here.
