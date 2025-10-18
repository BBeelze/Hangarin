from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from happ.models import Category
from happ.forms import CategoryForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Category
    context_object_name = 'home'
    template_name = 'home.html'

class CategoryList(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_list.html'
    paginate_by = 5

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')