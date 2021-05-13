from django.db import models
from django.shortcuts import render
from .models import Follower
from .forms import FollowerForm
from django.views.generic.edit import CreateView


# Create your views here.

class Follow(CreateView):
    """Отображение и обработка формы на странице"""
    model = Follower
    form_class = FollowerForm
    success_url = "/"
