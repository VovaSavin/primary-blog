from django.shortcuts import render, get_object_or_404
from .models import MessagesBetweenUsers
from .forms import MessagesForm
from django.views.generic import (
    ListView,
    DetailView
)
from django.utils import timezone
from django.views.generic.edit import CreateView, FormMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.


class MessagesList(LoginRequiredMixin, ListView):
    '''Отображение всех сообщений для пользователя'''
    model = MessagesBetweenUsers
    context_object_name = 'sms'
    template_name = 'messagesusers/message-list.html'

    def get_queryset(self, **kwargs):
        sett = MessagesBetweenUsers.objects.filter(Q(sender=self.request.user) | Q(addressee=self.request.user)).order_by('-date_message')
        return sett


    def get_context_data(self, **kwargs):
        context = super(MessagesList, self).get_context_data(**kwargs)
        context['title'] = 'Все сообщения'
        return context


class MessagesInboxList(LoginRequiredMixin, ListView):
    '''Отображение входящих сообщений для пользователя'''
    model = MessagesBetweenUsers
    context_object_name = 'sms'
    template_name = 'messagesusers/message-list.html'

    def get_queryset(self):
        return MessagesBetweenUsers.objects.filter(addressee=self.request.user).order_by('-date_message')
    
    def get_context_data(self, **kwargs):
        context = super(MessagesInboxList, self).get_context_data(**kwargs)
        context['title'] = 'Входящие сообщения'
        return context

class MessagesOutboxList(LoginRequiredMixin, ListView):
    '''Отображение исходящих сообщений пользователя'''
    model = MessagesBetweenUsers
    context_object_name = 'sms'
    template_name = 'messagesusers/message-list.html'

    def get_queryset(self):
        return MessagesBetweenUsers.objects.filter(sender=self.request.user).order_by('-date_message')

    def get_context_data(self, **kwargs):
        context = super(MessagesOutboxList, self).get_context_data(**kwargs)
        context['title'] = 'Отправленные сообщения'
        return context

class MessagesListUsers(LoginRequiredMixin, ListView, FormMixin):
    model = MessagesBetweenUsers
    context_object_name = 'mess'
    template_name = 'messagesusers/message-list-users.html'
    

    def get_queryset(self, **kwargs):
        my_recepient = get_object_or_404(
            User, username=self.kwargs.get('username'))
        my_sender = get_object_or_404(
            User, username=self.kwargs.get('username'))
        my_sent = MessagesBetweenUsers.objects.filter(
            sender=self.request.user).filter(addressee=my_recepient)
        my_received = MessagesBetweenUsers.objects.filter(
            addressee=self.request.user).filter(sender=my_sender)
        return my_sent | my_received.order_by('date_message')

    def get_context_data(self, **kwargs):
        context = super(MessagesListUsers, self).get_context_data(**kwargs)
        context['title'] = f'Диалог с {get_object_or_404(User, username=self.kwargs.get("username"))}'
        return context


class MessageDetail(LoginRequiredMixin, DetailView):
    '''Отображение конкретного сообщения'''
    model = MessagesBetweenUsers
    context_object_name = 'sms'
    template_name = 'messagesusers/message-detail.html'

    def get_context_data(self, **kwargs):
        context = super(MessageDetail, self).get_context_data(**kwargs)
        context['title'] = MessagesBetweenUsers.objects.get(
            pk=self.kwargs['pk'])
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
