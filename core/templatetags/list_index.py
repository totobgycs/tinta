from django import template
register = template.Library()

@register.filter(name='list_index')
def index(List, i):
    return List[int(i)]

