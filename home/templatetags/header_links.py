from django import template
from dashboard.models import SiteSetting

register = template.Library()


@register.inclusion_tag('header_links.html')
def show_header_links():
    SiteSetting.get('header_links')
    return {}
