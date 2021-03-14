from django.contrib import admin
from .models import MessagesBetweenUsers

# Register your models here.
@admin.register(MessagesBetweenUsers)
class MessagesBetweenUsersAdmin(admin.ModelAdmin):
    '''
    Регистрация модели в админ панели
    и расположение её полей
    '''
    list_display = ['sender', 'addressee', 'text_message', 'date_message']