from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# Só fizemos isso pq queremos que no admin apareça o campo personalizado: filme_vistos
campos = list(UserAdmin.fieldsets)
campos.append(('Histórico', {'fields': ('filme_vistos',)}))
UserAdmin.fieldsets = tuple(campos)
# Register your models here.


admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)