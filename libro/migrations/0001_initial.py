# Generated by Django 4.1.1 on 2022-09-29 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('tipo_documento', models.CharField(max_length=100)),
                ('numero_documento', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=2)),
                ('telefono', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('direccion', models.TextField(blank=True, max_length=100)),
                ('nacimiento', models.DateField(blank=True)),
                ('educacion', models.TextField(blank=True, max_length=100)),
                ('ocupacion', models.TextField(blank=True, max_length=100)),
                ('discapacidad', models.TextField(blank=True, max_length=100)),
                ('grupo_etnico', models.TextField(blank=True, max_length=100)),
                ('comision_trabajo', models.TextField(blank=True, max_length=100)),
                ('observaciones', models.TextField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
