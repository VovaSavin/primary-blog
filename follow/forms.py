from django import forms
from django.db import models
from django.forms import fields, widgets
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Follower


class FollowerForm(forms.ModelForm):
    """Форма для вывода на страницу поля с мейлом для подписчиков"""
    captca = ReCaptchaField()

    class Meta:
        model = Follower
        fields = ["e_mail", "captca", ]
        widgets = {
            "e_mail": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ваш Email...",
                }
            )
        }
        labels = {
            "e_mail": "",
        }
