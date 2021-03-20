from django import forms
from .models import MessagesBetweenUsers

class MessagesForm(forms.ModelForm):
    text_message = forms.CharField(
        label='Текст сообщения:',
        required=False,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Напишите сюда...', 'rows': 5}),
    )

    class Meta:
        model = MessagesBetweenUsers
        fields = ['text_message']