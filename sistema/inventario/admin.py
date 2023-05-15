from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
import datetime
from .forms import LoginFormulario
from .models import *

class UsuarioAdmin(UserAdmin):
    add_form = LoginFormulario
    #form = CustomUserChangeForm
    model = Usuario
    list_display = ['email', 'username',]

# Exportar Productos
#------------------------------------------------------------------------------------------------#
class ProductoResource(resources.ModelResource):
    categoria = fields.Field(attribute='get_categoria_display',column_name='Modelos')
    producto = fields.Field(attribute='descripcion',column_name='Materiales')
    stock = fields.Field(attribute='disponible',column_name='Stock')
    class Meta:
        model = Producto
        fields = ('categoria','producto', 'precio', 'stock')
        export_order = ('producto', 'precio', 'stock','categoria')

class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource
    readonly_fields = ('descripcion', 'precio', 'categoria')
    search_fields = ('descripcion', 'precio', 'categoria')
    list_display = ('descripcion', 'precio', 'disponible', 'categoria')


#------------------------------------------------------------------------------------------------#

# Exportar clientes
#------------------------------------------------------------------------------------------------#
class ClienteResource(resources.ModelResource):
    cedula = fields.Field(attribute='cedula',column_name='DNI')
    nombre = fields.Field(attribute='nombre',column_name='Nombre')
    apellido = fields.Field(attribute='apellido',column_name='Apellido')
    direccion = fields.Field(attribute='direccion',column_name='Direccion')
    nacimiento = fields.Field(attribute='nacimiento',column_name='Nacimiento')
    telefono = fields.Field(attribute='telefono',column_name='Telefono')
    correo = fields.Field(attribute='correo',column_name='Correo')

    class Meta:
        model = Cliente
        fields = ('cedula','nombre', 'apellido', 'direccion', 'nacimiento', 'telefono', 'correo')
        export_order = ('cedula','nombre', 'apellido', 'direccion', 'nacimiento', 'telefono', 'correo')

class ClienteAdmin(ImportExportModelAdmin):
    resource_class = ClienteResource
    readonly_fields = ('cedula','nombre', 'apellido', 'direccion', 'nacimiento', 'telefono', 'correo')
    search_fields = ('cedula','nombre', 'apellido', 'direccion', 'nacimiento', 'telefono', 'correo')
    list_display = ('cedula','nombre', 'apellido', 'direccion', 'nacimiento', 'telefono', 'correo')
#------------------------------------------------------------------------------------------------#
# Exportar Provedores
#------------------------------------------------------------------------------------------------#
class ProveedorResource(resources.ModelResource):
    cedula = fields.Field(attribute='cedula',column_name='RUC')
    nombre = fields.Field(attribute='nombre',column_name='Empresa')
    direccion = fields.Field(attribute='direccion',column_name='Direccion')
    telefono = fields.Field(attribute='telefono',column_name='Telefono')
    correo = fields.Field(attribute='correo',column_name='Correo')

    class Meta:
        model = Proveedor
        fields = ('cedula','nombre', 'direccion', 'telefono', 'correo')
        export_order = ('cedula','nombre', 'direccion', 'telefono', 'correo')

class ProveedorAdmin(ImportExportModelAdmin):
    resource_class = ProveedorResource
    readonly_fields = ('cedula','nombre', 'direccion', 'telefono', 'correo')
    search_fields = ('cedula','nombre', 'direccion', 'telefono', 'correo')
    list_display = ('cedula','nombre', 'direccion', 'telefono', 'correo')
#------------------------------------------------------------------------------------------------#


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Pedido)
admin.site.register(Factura)
admin.site.register(Opciones)
