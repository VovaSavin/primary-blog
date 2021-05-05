from django.shortcuts import render, get_object_or_404, redirect
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
from django.core.exceptions import ValidationError




# Create your views here.

class MessagesList(LoginRequiredMixin, ListView):
    '''Отображение всех сообщений для пользователя'''
    model = MessagesBetweenUsers
    context_object_name = 'sms'
    template_name = 'messagesusers/message-list.html'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        sett = MessagesBetweenUsers.objects.filter(Q(sender=self.request.user) | Q(
            addressee=self.request.user)).order_by('-date_message')
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
    form_class = MessagesForm

        


    def get_success_url(self, **kwargs):
        return reverse_lazy('your-messages-user', kwargs={'username': self.kwargs.get('username')})


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        self.object.addressee = get_object_or_404(
            User, username=self.kwargs.get('username'))
        self.object.date_message = timezone.now()
        self.object.save()
        return super().form_valid(form)


    def get_queryset(self, **kwargs):
        my_recepient = get_object_or_404(
            User, username=self.kwargs.get('username'))
        my_sender = get_object_or_404(
            User, username=self.kwargs.get('username'))
        my_sent = MessagesBetweenUsers.objects.filter(
            sender=self.request.user, addressee=my_recepient).select_related('sender', 'addressee')
        my_received = MessagesBetweenUsers.objects.filter(
            addressee=self.request.user, sender=my_sender).select_related('addressee', 'sender')
        return my_sent | my_received.order_by('date_message')
        #return super().get_queryset() Реализовать переадресацию, что бы текущий пользователь не мог переписываться сам с собой.


    def get_context_data(self, **kwargs):
        context = super(MessagesListUsers, self).get_context_data(**kwargs)
        context['title'] = f'Диалог с {get_object_or_404(User, username=self.kwargs.get("username"))}'
        i_message = MessagesBetweenUsers.objects.filter(sender=self.request.user).select_related('addressee')
        me_message = MessagesBetweenUsers.objects.filter(addressee=self.request.user).select_related('sender')
        friends = set()
        for x in i_message:
            friends.add(x.addressee)
        for y in me_message:
            friends.add(y.sender)
        context['frnds'] = friends
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
        if form.instance.addressee == self.request.user:
            form.save(commit=False)
            return redirect(reverse_lazy('message-writing'))
        form.instance.date_message = timezone.now()
        return super().form_valid(form)


def message_delete(request, pk, type, *args):
    '''Delete messages for request user'''
    my_messages = MessagesBetweenUsers.objects.get(pk=pk)
    name = User.objects.get(username=my_messages.addressee)
    if type == 'deletemymessage':
        my_messages.delete()
        return redirect(reverse_lazy('your-messages-user', args=[str(name)]))
    else:
        return redirect(reverse_lazy('your-messages-user', args=[str(name)]))
    context = {
        'message': my_messages,
    }
    return render(request, 'messagesusers/message-delete.html', context)


