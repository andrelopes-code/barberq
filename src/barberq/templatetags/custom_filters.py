from django import template

register = template.Library()


@register.filter
def addclass(field, classes):
    if not hasattr(field, 'as_widget'):
        return field
    return field.as_widget(attrs={'class': classes})
