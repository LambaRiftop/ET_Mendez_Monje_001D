from django.db import models
import datetime
import random

class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=50, verbose_name='Email')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    password = models.CharField(max_length=20, verbose_name='Password')
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria = models.CharField(max_length=25, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    # Campos del modelo
    codigo = models.CharField(max_length=20, primary_key=True, verbose_name='Código del producto')
    nombre = models.CharField(max_length=100, verbose_name='Nombre del producto')
    descripcion = models.TextField(verbose_name='Descripción del producto')
    precio = models.IntegerField(default=0, verbose_name='Precio')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name='Categoria')
    
    # Método para generar código de producto
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = str(random.randint(1000, 9999))  # Genera código de 4 dígitos
        super().save(*args, **kwargs)

    # metodo para colocar un punto en el precio despues de los primeros 3 digitos
    def precio_concat(self):
        precio = str(self.precio)
        if len(precio) > 3:
            precio = precio[:-3] + '.' + precio[-3:]
        return precio

    # Método para mostrar nombre del producto en el panel de administrador
    def __str__(self):
        return self.nombre
    
class Boleta(models.Model):
    idBoleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)

    def __str__(self):
        return str(self.idBoleta)
    
class DetalleBoleta(models.Model):
    idBoleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    idDetalle = models.AutoField(primary_key=True)
    codigo = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.idDetalle)
    
#modelos de la api
class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    imagenAPI = models.ImageField(upload_to="imagenesAPI", null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return str(self.idImagen)