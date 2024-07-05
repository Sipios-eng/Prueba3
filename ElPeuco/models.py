from django.db import models

# Create your models here.

class platos(models.Model):
    id_platos = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=150)
    descripcion_plato = models.CharField(max_length=150)
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='images/')