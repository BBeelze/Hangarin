from django.forms import ModelForm
from django import forms
from happ.models import Category, Note, Priority, SubTask, Task

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"