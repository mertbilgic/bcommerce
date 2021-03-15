from django import template
register = template.Library()

@register.simple_tag
def define_item_id(val=None):
  return f"item-{val}"