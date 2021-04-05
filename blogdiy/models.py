from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Bloger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, verbose_name='Имя', blank=True, null=True)
    surname = models.CharField(
        max_length=100, verbose_name='Фамилия', blank=True, null=True)
    age = models.PositiveIntegerField(
        verbose_name='Возвраст', blank=True, null=True)
    about = models.TextField(verbose_name='Инфо', blank=True, null=True)
    foto = models.ImageField('Фото профиля',
                             default='foto-users/nofoto.png', upload_to='foto-users/')

    def save(self, *args, **kwargs):
        super().save()
        img_root = Image.open(self.foto.path)
        if img_root.width > 200 or img_root.height > 200:
            new_size = (200, 200)
            img_root.thumbnail(new_size)
            img_root.save(self.foto.path)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_absolute_url(self):
        return reverse('blogers-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Блоггер'
        verbose_name_plural = 'Блоггеры'


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема')
    author_blog = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    text_blog = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    picture_blog = models.ImageField(verbose_name='Изображение', default='photo_blog/no-foto.gif', upload_to='photo_blog/')

    def save(self, *args, **kwargs):
        super().save()
        img_root = Image.open(self.picture_blog.path)
        if img_root.width > 766 or img_root.height > 423:
            new_size = (766, 423)
            img_root.thumbnail(new_size)
            img_root.save(self.picture_blog.path)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blogs-all')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class Comments(models.Model):
    text_comments = models.TextField(verbose_name='Комментарий', )
    to_blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, verbose_name='Для статьи')
    author_comments = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    date_comment = models.DateTimeField(
        default=timezone.now, verbose_name='Дата')

    def __str__(self):
        return f'{self.author_comments} к {self.to_blog}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date_comment']

class RaitingVal(models.Model):
    '''Числовые значения рейтинга записей'''
    val = models.SmallIntegerField(verbose_name='Значение рейтинга', default=0)

    def __str__(self):
        return self.val
    
    class Meta:
        verbose_name = 'Значение рейтинга'
        verbose_name_plural = 'Значение рейтинга' 

class Raiting(models.Model):
    '''Сам рейтинг'''
    who_like = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто')
    how_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Какой блог')
    value = models.ForeignKey(RaitingVal, on_delete=models.CASCADE, verbose_name='Значение')

    def __str__(self):
        return f'{self.who_like}->{self.how_blog}'

    class Meta:
        verbose_name = 'Рейтинг блога'
        verbose_name_plural = 'Рейтинг блога' 