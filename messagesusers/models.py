from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class MessagesBetweenUsers(models.Model):
    '''Модель для сообщений'''
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sender', verbose_name='Отправитель')
    addressee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_addressee', verbose_name='Получатель')
    text_message = models.TextField(verbose_name='Текст сообщения')
    date_message = models.DateTimeField(default=timezone.now, verbose_name='Дата отправки')

    def __str__(self):
        return f'{self.sender} к {self.addressee}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'