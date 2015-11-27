# from django.template.defaultfilters import register
# from django.template.defaulttags import register
from django import template

register = template.Library()


@register.filter(name='get')
def get(d, k):
    return d.get(k, None)