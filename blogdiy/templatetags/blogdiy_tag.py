from django import template
from blogdiy.models import Blog
from blogdiy.forms import SendForm

register = template.Library()


@register.inclusion_tag('blogdiy/tags/last-blog.html')
def get_last_blog():
    """Возвращает последних два блога, опубликованных на сайте"""
    lstblog = Blog.objects.order_by('-date')[:2]
    return {'lastblog': lstblog}


@register.inclusion_tag('blogdiy/tags/send-form.html')
def get_send_form():
    """Возвращает форму для отправки сообщений на почту"""
    return {'sendform': SendForm()}
