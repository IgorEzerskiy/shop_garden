from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    query = context['request'].GET.copy()

    if 'page' in query:
        query.pop('page')

    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()
