# Generated by Django 4.1.1 on 2022-09-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliado',
            name='numero_documento',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='afiliado',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
