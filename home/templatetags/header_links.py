from django import template
from dashboard.models import PagePos

register = template.Library()


@register.inclusion_tag('header_links.html')
def show_header_links():
    header_pos = PagePos.objects.get_headers()
    return locals()
