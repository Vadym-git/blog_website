from django import template
from post.models import Categories, Post

register = template.Library()


@register.simple_tag
def categories():
    return Categories.objects.all()


@register.simple_tag
def posts():
    return Post.objects.all().order_by('-reg_date')[:12]
