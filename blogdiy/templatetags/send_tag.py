from django import template
from blogdiy.forms import SendForm

register = template.Library()


@register.inclusion_tag('blogdiy/tags/send-form.html')
def get_send_form():
    """Возвращает форму для отправки сообщений на почту"""
    return {'sendform': SendForm()}
