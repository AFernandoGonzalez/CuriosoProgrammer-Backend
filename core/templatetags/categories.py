from django import template
register = template.Library()

from blog.models import Category

@register.inclusion_tag("./core/base.html")
def footer():
    category = Category.objects.all()
    return {"category": category}