from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

from .forms import LoginFormulario
from .models import *

class UsuarioAdmin(UserAdmin):
    add_form = LoginFormulario
    #form = CustomUserChangeForm
    model = Usuario
    list_display = ['email', 'username',]


class ProductoResource(resources.ModelResource):
    categoria = fields.Field(attribute='get_categoria_display')
    producto = fields.Field(attribute='descripcion',column_name='Producto')
    stock = fields.Field(attribute='disponible',column_name='Stock')
    class Meta:
        model = Producto
        fields = ('categoria', 'id', 'producto', 'precio', 'stock')
        export_order = ('id', 'producto', 'precio', 'stock','categoria')

class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource
    readonly_fields = ('descripcion', 'precio', 'categoria')
    search_fields = ('descripcion', 'precio', 'categoria')
    list_display = ('descripcion', 'precio', 'disponible', 'categoria')
 
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor)
admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Opciones)
