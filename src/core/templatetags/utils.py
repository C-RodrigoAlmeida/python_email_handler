from django import template

register = template.Library()

@register.filter
def getattr(obj, attr):
    return getattr(obj, attr)