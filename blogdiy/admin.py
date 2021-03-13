from django.contrib import admin
from .models import (
    Blog,
    Bloger,
    Comments,
)

# Register your models here.


@admin.register(Bloger)
class BlogerAdmin(admin.ModelAdmin):
    '''Зарегистрировали модель Bloger и расширим поля в админ странице'''
    list_display = ('name', 'surname', 'age', 'foto')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    '''Зарегистрировали модель Blog и расширим поля в админ странице'''
    list_display = ('title', 'author_blog', 'date')
    

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    '''Зарегистрировали модель Comments и расширим поля в админ странице'''
    list_display = ('author_comments', 'to_blog', 'date_comment')

