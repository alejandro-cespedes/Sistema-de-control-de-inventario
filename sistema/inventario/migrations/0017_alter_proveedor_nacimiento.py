# Generated by Django 3.2 on 2023-05-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0016_alter_proveedor_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='nacimiento',
            field=models.DateField(null=True),
        ),
    ]