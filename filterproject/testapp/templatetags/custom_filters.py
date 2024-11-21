from django import template

register = template.Library()

@register.filter(name='fupper')
def first_five_upper(value):
    """Returns the first five characters in uppercase."""
    return value[:5].upper()
