from django import forms
from .models import Usuario
from django.conf import settings
from .models import Producto


class UsuarioForm(forms.ModelForm):
    admin_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña de administrador (opcional)'
        }),
        required=False,
        label="¿Quieres ser admin?"
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_admin_password(self):
        admin_pass = self.cleaned_data.get('admin_password')
        if admin_pass and admin_pass != settings.ADMIN_REGISTER_PASSWORD:
            raise forms.Valid

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock', 'categoria']
        labels = {
            'nombre':'Nombre',
            'precio':'Precio',
            'descripcion':'Descripcion',
            'sttock':'Stock',
            'categoria':'Categoria'
        }

        precio_concat = Producto.precio_concat

        widgets = {
            'nombre': forms.TextInput(attrs={'id':'nombre','class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'precio': forms.NumberInput(attrs={'id':'precio','class': 'form-control', 'placeholder': 'Precio del producto'}),
            'descripcion': forms.Textarea(attrs={'id':'nombre','class': 'form-control', 'placeholder': 'Descripción'}),
            'stock': forms.NumberInput(attrs={'id':'nombre','class': 'form-control', 'placeholder': 'Stock'}),
            'categoria': forms.Select(attrs={'id':'nombre','class': 'form-control', 'placeholder': 'Selecione Categoria'}),
        }

            
            