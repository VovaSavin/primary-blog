from django.db import models


# Create your models here.

class Currency(models.Model):
    '''Currency'''
    currency_value = models.CharField(verbose_name='Валюты', max_length=300)

    def __str__(self):
        return f'{self.currency_value}'

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'