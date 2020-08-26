from blogapp.models import Post
from django import template
register=template.Library()

@register.simple_tag
def totalposts():
    return Post.objects.count()
