from django import forms
from .models import Bloger, Comments
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class EditProfile(forms.ModelForm):
    email = forms.EmailField(
        label='Ваш Email:',
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите Email'}),
    )
    username = forms.CharField(
        label='Ваш логин:',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
    )

    class Meta:
        model = User
        fields = ['email', 'username']


class EditBlogerProfile(forms.ModelForm):
    name = forms.CharField(
        label='Имя:',
        required=False,
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
    )
    surname = forms.CharField(
        label='Фамилия:',
        required=False,
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваша фамилия'}),
    )
    age = forms.CharField(
        label='Возраст:',
        required=False,
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ваш возраст'}),
    )
    about = forms.CharField(
        label='О себе:',
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': '''Напишите что-нибудь о себе... Например: Безработный сыч,
             живущий до сих пор с родителями'''}),
    )
    def clean_age(self):
        data = self.cleaned_data['age']
        if int(data) < 0:
            raise ValidationError('Возраст не может быть отрицательным')
        return data
    class Meta:
        model = Bloger
        fields = ['name', 'surname', 'age', 'about']


class CommentsForm(forms.ModelForm):
    text_comments = forms.CharField(
        label = 'Текст комментария',
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Оставь своё не нужное мнение...', 'rows': 5}
        )
    )
    class Meta:
        model = Comments
        fields = ['text_comments']

