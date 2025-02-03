from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404 # Importar para manejar errores 404
from .models import Usuario, Producto, Boleta, DetalleBoleta
from .forms import ProductoForm
from core.shopping import Carrito

def home(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def galeria(request):
    return render(request, 'galeria.html')

def tienda(request):
    return render(request, 'tienda.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})

def registro(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

# Registra un usuario
def registro_usuario(request):
    if request.method == 'POST':
        # Capturar datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        admin_password = request.POST.get('admin_password', '')
        
        errores = []

        # Validaciones básicas
        if password != confirm_password:
            errores.append("Las contraseñas no coinciden")
            
        if Usuario.objects.filter(email=email).exists():
            errores.append("El correo ya está registrado")

        # Validar contraseña maestra si se ingresó
        is_admin = False
        if admin_password:
            if admin_password != "clavemaestra123":  # Cambia por tu contraseña
                errores.append("Contraseña de administrador incorrecta")
            else:
                is_admin = True

        # Manejar errores
        if errores:
            for error in errores:
                messages.error(request, error)
            return redirect('registro_usuario')

        # Crear usuario
        try:
            usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password,
                is_admin=is_admin
            )
            usuario.save()
            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión")
            return redirect('login')
            
        except Exception as e:
            messages.error(request, f"Error al registrar: {str(e)}")
            return redirect('registro_usuario')

    return render(request, 'register.html')


# Iniciar sesión
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.password == password:
                request.session['usuario_id'] = usuario.email
                request.session['is_admin'] = usuario.is_admin 
                return redirect('index')
            else:
                messages.error(request, "Contraseña incorrecta")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario no registrado")
        
        return redirect('login')

    return render(request, 'login.html')

# Cerrar sesión
def logout(request):
    request.session.flush()
    return redirect('index')


# seccion de admin para el Crud de productos
def adminCRUD(request):
    if not request.session.get('is_admin'):
        return redirect('home')
    
    productos = Producto.objects.all()
    return render(request, 'admin_panel.html', {'productos': productos})

def crear_producto(request):
    if not request.session.get('is_admin'):
        return redirect('home')
    
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminCRUD')
    else:
        form = ProductoForm()
    return render(request, 'form_producto.html', {'form': form})

def editar_producto(request, id):
    if not request.session.get('is_admin'):
        return redirect('home')
    
    producto = get_object_or_404(Producto, codigo=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('adminCRUD')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'form_producto.html', {'form': form})

def eliminar_producto(request, id):
    if not request.session.get('is_admin'):
        return redirect('home')
    
    producto = get_object_or_404(Producto, codigo=id)
    producto.delete()
    return redirect('adminCRUD')

def tienda(request):
    query = request.GET.get('q')
    artesanias = Producto.objects.all()
    if query:
        artesanias = artesanias.filter(nombre__icontains=query)
    
    data = {
        'artesanias': artesanias,
        'query': query
    }
    return render(request, 'tienda.html', data)

def agregar(request, id):
    carrito=Carrito(request)
    artesania = Producto.objects.get(codigo = id)
    carrito.agregar(artesania=artesania)
    return redirect('tienda')

def eliminar(request, id):
    carrito = Carrito(request)
    artesania = Producto.objects.get(codigo = id)
    carrito.eliminar(artesania=artesania)
    return redirect('tienda')

def restar(request, id):
    carrito = Carrito(request)
    artesania = Producto.objects.get(codigo = id)
    carrito.restar(artesania=artesania)
    return redirect('tienda')

def limpiar(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tienda')

def generarBoleta(request):
    precio_subtotal = 0
    precio_impuesto = 0
    precio_total = 0

    for key, value in request.session['carrito'].items():
        precio_impuesto += int(value['precio']) * int(value["cantidad"])
    
    precio_total = round(precio_impuesto * 1.25)
    boleta = Boleta(total=precio_total)
    boleta.save()

    productos = []
    for key, value in request.session['carrito'].items():
        articulo = Producto.objects.get(codigo=value['codigo'])
        cant = value['cantidad']
        precio_subtotal = cant * int(value['precio'])

        if articulo.stock >= cant:
            articulo.stock -= cant
            articulo.save()
        else:
            messages.error(request, f"Stock insuficiente para {articulo.nombre}. Solo quedan {articulo.stock} unidades.")
            return redirect('carrito')

        # Guardar en DetalleBoleta
        detalle = DetalleBoleta(idBoleta=boleta, codigo=articulo, cantidad=cant, subtotal=precio_subtotal)
        detalle.save()
        productos.append(detalle)

    data = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'subtotal': precio_subtotal,
        'total': boleta.total
    }

    request.session['boleta'] = boleta.idBoleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html', data)

def eliminar_articulo(request, id):
    if 'usuario_id' not in request.session:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect('login')

    articulo = get_object_or_404(DetalleBoleta, id=id)
    articulo.delete()
    
    messages.success(request, "Artículo eliminado correctamente.")
    return redirect('detalle_compra')
