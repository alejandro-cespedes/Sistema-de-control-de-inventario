from django import template

register = template.Library()

@register.filter(name='calcular_precio_unitario')
def calcular_precio_unitario(total, cantidad):
    return total / cantidad

@register.filter(name='restar')
def restar(sub_total, total):
    return sub_total - total