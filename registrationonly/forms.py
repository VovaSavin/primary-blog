from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationCustomForm(UserCreationForm):
    '''Поле для регистрации пользователя на стороне клиента'''
    email = forms.EmailField(
        label='Ваш Email:',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}),
        )
    username = forms.CharField(
        label='Ваш логин:',
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
        )
    password1 = forms.CharField(
        label='Введите пароль:',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль:',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        

