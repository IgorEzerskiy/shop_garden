from django import template

register = template.Library()


@register.filter(name='replace_data_if_value_none')
def replace_data_if_value_none(value):
    if value is None:
        return 'Немає значення'
    return value
