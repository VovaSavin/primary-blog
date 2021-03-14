from django.shortcuts import render
from .models import MessagesBetweenUsers
from django.views.generic import (
    ListView,
    DetailView
)
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class MessagesList(LoginRequiredMixin, ListView):
    '''Отображение всех сообщений для пользователя'''
    model = MessagesBetweenUsers
    context_object_name = 'sms'
    template_name = 'messagesusers/message-list.html'

    def get_queryset(self):
        my_sent = MessagesBetweenUsers.objects.filter(sender=self.request.user)
        my_received = MessagesBetweenUsers.objects.filter(addressee=self.request.user)
        return my_sent | my_received.order_by('-date_message')

    def get_context_data(self, **kwargs):
        context = super(MessagesList, self).get_context_data(**kwargs)
        context['title'] = 'Ваши сообщения'
        return context


class MessageDetail(LoginRequiredMixin, DetailView):
    '''Отображение конкретного сообщения'''
    model = MessagesBetweenUsers
    context_object_name = 'sms'
    template_name = 'messagesusers/message-detail.html'

    def get_context_data(self, **kwargs):
        context = super(MessageDetail, self).get_context_data(**kwargs)
        context['title'] = MessagesBetweenUsers.objects.get(pk=self.kwargs['pk'])
        return context


class MessageCreate(LoginRequiredMixin, CreateView):
    '''Создания сообщения для отправки'''
    model = MessagesBetweenUsers
    template_name = 'messagesusers/message-writing.html'
    fields = ['addressee', 'text_message']
    success_url = reverse_lazy('your-messages')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.date_message = timezone.now()
        return super().form_valid(form)
