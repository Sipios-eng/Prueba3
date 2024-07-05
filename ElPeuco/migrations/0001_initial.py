# Generated by Django 5.0.6 on 2024-07-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='platos',
            fields=[
                ('id_platos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_plato', models.CharField(max_length=150)),
                ('descripcion_plato', models.CharField(max_length=150)),
                ('precio', models.IntegerField()),
                ('foto', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
