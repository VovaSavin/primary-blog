from django.contrib import admin
from .models import Follower

# Register your models here.


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    """Модель Follower в админке"""
    list_display = [
        "e_mail", "date",
    ]
