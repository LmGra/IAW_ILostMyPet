from django.contrib import admin

#from .models import Mascotas
#from .models import Perdidos
#from .models import Encuentros
#from .models import Area
#from .models import Usuarios
#from .models import User

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

admin.site.register(Mascotas)
admin.site.register(Perdidos)
admin.site.register(Encuentros)
#admin.site.register(Area)
#admin.site.register(Usuarios)
admin.site.register(User)

#class UsuarioInline(admin.StackedInline):
    #model = Usuarios
#    model = User
#    can_delete= False
#    verbose_name_plural = 'usuario'

#class UserAdmin(BaseUserAdmin):
#    inlines = (UsuarioInline,)

#admin.site.unregister(User)
#admin.site.register(User,UserAdmin)
