from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['descripcion_producto', 'nombre_producto', 'precio', 'foto']

class FormularioRegistrousuarioRegistrado(UserCreationForm):
    class Meta:
        model = usuarioRegistrado
        fields = ['email', 'first_name', 'last_name', 'phone', 'birth_date', 'address', 'postal_code','password1', 'password2']
        widgets ={
            'email': forms.EmailInput,
            'first_name':forms.TextInput, 
            'last_name':forms.TextInput, 
            'phone':forms.TextInput(attrs={'type': 'tel'}), 
            'birth_date':forms.DateInput(attrs={'type': 'date'}), 
            'address':forms.TextInput, 
            'postal_code':forms.NumberInput,
            'password1':forms.PasswordInput, 
            'password2':forms.PasswordInput,
        }

    def __init__(self, *args, **kwargs):
        super(FormularioRegistrousuarioRegistrado, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'id': 'id_correo', 'name': 'correo', 'placeholder': 'Ingresa correo','class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'id': 'id_nombre', 'name': 'nombre', 'placeholder': 'Escribe tu nombre','class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'id': 'id_apellido', 'name': 'apellido', 'placeholder': 'Escribe tu apellido','class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'id': 'id_telefono', 'name': 'telefono', 'placeholder': '56912345678','class': 'form-control'})
        self.fields['birth_date'].widget.attrs.update({'id': 'id_fecha_nacimiento', 'name': 'fecha_nacimiento','type': 'date','class': 'form-control', 'placeholder': 'YYYY/MM/DD',})
        self.fields['address'].widget.attrs.update({'id': 'id_direccion', 'name': 'direccion', 'placeholder': 'Ingresa tu direccion','class': 'form-control'})
        self.fields['postal_code'].widget.attrs.update({'id': 'id_codigo_postal', 'name': 'codigo_postal', 'placeholder': '1234567','class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'id': 'id_password1', 'name': 'password1', 'placeholder': 'ingresa contraseña','class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'id': 'id_password2', 'name': 'password2', 'placeholder': 'Confirma tu contraseña','class': 'form-control'})

class FormularioInicioSesion(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioInicioSesion, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Correo"
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Correo'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})


class UserForm(forms.ModelForm):
    class Meta:
        model = usuarioRegistrado
        fields = ['first_name', 'last_name', 'email']


class ContactoForms(forms.ModelForm):
    class Meta:
        model = Apedido
        fields = ['Correo_pedido', 'Titulo_Pedido', 'descripcion_pedido', 'Imagen_Adjunta']
        widgets ={
            'Correo_pedido': forms.EmailInput(attrs={'class': 'form-control'}),
            'Titulo_Pedido':forms.TextInput(attrs={'class': 'form-control'}), 
            'descripcion_pedido':forms.Textarea(attrs={'class': 'form-control'}),
        }