from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User

class AdministradorusuarioRegistrado(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo de correo electrónico debe estar establecido')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class usuarioRegistrado(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=7)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AdministradorusuarioRegistrado()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'birth_date', 'address', 'postal_code']

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    run = models.CharField(max_length=12)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    document_number = models.CharField(max_length=20)

class producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion_producto = models.CharField(max_length=60)
    nombre_producto = models.CharField(max_length=30)
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.id_producto

class Carrito(models.Model):
    user = models.OneToOneField(usuarioRegistrado, on_delete=models.CASCADE)
    created_el = models.DateTimeField(auto_now_add=True)

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
class Apedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    Correo_pedido = models.EmailField()
    Titulo_Pedido = models.CharField(max_length=60)
    descripcion_pedido =  models.TextField()
    Imagen_Adjunta = models.ImageField(upload_to='images/')
