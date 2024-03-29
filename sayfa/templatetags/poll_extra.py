from django import template

register = template.Library()


@register.filter(name='shorterArt')
def shorterArt(value, arg):
    return value[:arg] + '...' if len(value) > 30 else value[:arg]


@register.filter(name='NewsFilter')
def NewsFilter(value, arg):
    return value[:arg] + '...' if len(value) > 25 else value[:arg]


@register.filter(name="NewsTitle")
def NewsTitle(value, arg):
    return value[:arg] + '...' if len(value) > 10 else value[:arg]