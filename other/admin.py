from django.contrib import admin
from .models import Currency

# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    '''Зарегистрировали модель Currency и расширим поля в админ странице'''
    list_display = ('currency_value',)