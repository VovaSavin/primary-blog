from django.urls import path
from .import views

urlpatterns = [
    path('', views.registration_custom, name='registrate'),
]