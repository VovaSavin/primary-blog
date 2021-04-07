from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    Blog,
    Bloger,
    Comments,
    RaitingVal,
    Raiting,
)

# Register your models here.


@admin.register(Bloger)
class BlogerAdmin(admin.ModelAdmin):
    '''Зарегистрировали модель Bloger и расширим поля в админ странице'''
    list_display = ('name', 'surname', 'age',
                    'get_image')  # Вместо поля с изображением добавляем метод возврата url на фото

    def get_image(self, obj):
        '''Method for display profile image in admin-panel'''
        return mark_safe(f'<img src={obj.foto.url} width="25" height="30">')

    get_image.short_description = 'Фото профиля'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    '''Зарегистрировали модель Blog и расширим поля в админ странице'''
    list_display = ('title', 'author_blog', 'date', 'get_image')
    list_filter = ('author_blog',)  # Фильтрация в админке по данным полям

    def get_image(self, obj):
        '''Method for display blog image in admin-panel'''
        return mark_safe(f'<img src={obj.picture_blog.url} width="30" height="25">')

    get_image.short_description = 'Изображение'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    '''Зарегистрировали модель Comments и расширим поля в админ странице'''
    list_display = ('author_comments', 'to_blog', 'date_comment')


@admin.register(RaitingVal)
class RaitingValAdmin(admin.ModelAdmin):
    '''Значение рейтинга в админ панели'''
    list_display = (
        'val',
    )


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    '''Таблица рейтинга в админ.панели'''
    list_display = ('who_like', 'how_blog')
    # Фильтрация в админке по данным полям
    list_filter = ('who_like', 'how_blog')
