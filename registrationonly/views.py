from django.shortcuts import render, redirect
from .forms import RegistrationCustomForm
from django.urls import reverse


# Create your views here.


def registration_custom(request):
    '''Регистрация пользователя на стороне клиента'''
    if request.method == 'POST':
        form = RegistrationCustomForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect(reverse('login'))
    else:
        form = RegistrationCustomForm()
    context = {
        'title': 'Регистрация',
        'forms': form,
    }
    return render(request, 'registrationonly/registration-custom.html', context)
