from django.contrib import admin
from .models import Vehiculo, Reseña, MensajeDirecto, PerfilUsuario, Marca


admin.site.register(Vehiculo)
admin.site.register(Reseña)
admin.site.register(MensajeDirecto)
admin.site.register(PerfilUsuario)
admin.site.register(Marca)
