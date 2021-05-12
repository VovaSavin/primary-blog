from django.db import models

# Create your models here.


class Follower(models.Model):
    """Модель для хранения имя и мейла тех кто подписался"""
    e_mail = models.EmailField(verbose_name="Email", unique=True)
    name = models.CharField(
        verbose_name="Имя", max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.e_mail}'

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
