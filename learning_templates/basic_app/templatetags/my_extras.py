from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

@register.filter
def lower(value):
    return value.lower()

# Instead of this below statement we can use decorators that belongs to python and decorators are cleary define in django lecture
# register.filter('cut',cut)
