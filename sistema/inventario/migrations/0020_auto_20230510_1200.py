# Generated by Django 3.2 on 2023-05-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0019_auto_20230510_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono2',
            field=models.CharField(max_length=20, null=True),
        ),
    ]