from django import template
from ..forms import FollowerForm

register = template.Library()


@register.inclusion_tag("follow/tag/follow-form.html")
def get_form_follower():
    """Вернёт форму по ключу"""
    return {"form_follow": FollowerForm()}
