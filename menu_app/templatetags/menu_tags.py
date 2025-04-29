from django import template
from menu_app.models import MenuItem
from django.urls import resolve, Resolver404

register = template.Library()

@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    active_items = set()
    for item in menu_items:
        item.url = item.get_url()
        if item.url.strip('/') == current_url.strip('/') or (item.named_url.strip('/') and item.named_url.strip('/') in current_url.strip('/')):
            active_items.add(item)

    return {'menu_items': menu_items, 'active_items': active_items}