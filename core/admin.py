from django.contrib import admin
from .models import Usuario, Producto, Categoria, Boleta, DetalleBoleta

# Register your models here
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)