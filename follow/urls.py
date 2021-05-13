from django.urls import path
from . import views

urlpatterns = [
    path('', views.Follow.as_view(), name='follow'),
]
