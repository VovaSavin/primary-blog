from modeltranslation import fields
from modeltranslation.translator import register, TranslationOptions
from .models import Bloger


@register(Bloger)
class BlogerTranslationOptions(TranslationOptions):
    """Регистрация модели для перевода"""
    fields = ("name", "surname")
