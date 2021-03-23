from django.urls import path
from .import views

urlpatterns = [
    path('all', views.MessagesList.as_view(), name='your-messages'),
    path('inbox', views.MessagesInboxList.as_view(), name='your-messages-inbox'),
    path('outbox', views.MessagesOutboxList.as_view(), name='your-messages-outbox'),
    path('writing-message', views.MessageCreate.as_view(), name='message-writing'),
    path('<int:pk>', views.MessageDetail.as_view(), name='one-message'),
    path('<str:username>', views.MessagesListUsers.as_view(), name='your-messages-user'),
    path('<int:pk>/<slug:type>', views.message_delete, name='delete-message'),
]