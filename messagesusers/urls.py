from django.urls import path
from .import views

urlpatterns = [
    path('', views.MessagesList.as_view(), name='your-messages'),
    path('writing-message', views.MessageCreate.as_view(), name='message-writing'),
    path('<int:pk>', views.MessageDetail.as_view(), name='one-message'),
    path('<int:pk>', views.MessageDetail.as_view(), name='one-message'),
    path('<str:username>', views.MessagesListUsers.as_view(), name='your-messages-user'),
]