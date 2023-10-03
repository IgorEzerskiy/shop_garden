from django import template

register = template.Library()


@register.filter(name='custom_length')
def length(value):
    """Return the length of the value - useful for lists."""
    res = []
    try:
        for item in value:
            if item.index is True:
                res.append(item)
        return len(res)
    except (ValueError, TypeError):
        return 0
