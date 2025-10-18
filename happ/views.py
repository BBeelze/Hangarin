from django.shortcuts import render
from django.views.generic.list import ListView
from happ.models import Category

class HomePageView(ListView):
    model = Category
    context_object_name = 'home'
    template_name = 'home.html'