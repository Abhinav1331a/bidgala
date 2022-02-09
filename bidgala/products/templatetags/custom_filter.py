from django import template
from accounts.models import Material
from accounts.models import Style

register = template.Library()


@register.filter(name='get_style_details')
def get_style_details(value, key):
    """
        This is used to return the Syle values
    """
    if (value is not None) :
        value = value.replace('[','').replace(']','')
        if len(value) > 1:
            style = Style.objects.all()
            value = value.split(',')
            ids = [int(i) for i in value]
            style_details = Style.objects.filter(id__in = ids)
            return style_details
    
    return None

