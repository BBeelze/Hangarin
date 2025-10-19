"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from happ.views import HomePageView, CategoryList, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, NoteList, NoteCreateView, NoteUpdateView, NoteDeleteView, PriorityList, PriorityCreateView, PriorityUpdateView, PriorityDeleteView, SubTaskList, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView
from happ import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),

    # CATEGORY
    path('category_list', CategoryList.as_view(), name='category-list'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>',CategoryUpdateView.as_view(), name='category-update'),    
    path('category_list/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),

    #NOTES
    path('note_list', NoteList.as_view(), name='note-list'),
    path('note_list/add', NoteCreateView.as_view(), name='note-add'),
    path('note_list/<pk>',NoteUpdateView.as_view(), name='note-update'),    
    path('note_list/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'),

    #Priority
    path('priority_list', PriorityList.as_view(), name='priority-list'),
    path('priority_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<pk>',PriorityUpdateView.as_view(), name='priority-update'),    
    path('priority_list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),

    #SUBTASK
    path('subtask_list', SubTaskList.as_view(), name='subtask-list'),
    path('subtask_list/add', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<pk>',SubTaskUpdateView.as_view(), name='subtask-update'),    
    path('subtask_list/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),
]

