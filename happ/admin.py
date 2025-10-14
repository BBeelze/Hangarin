from django.contrib import admin
from .models import Category, Priority, Task, SubTask, Note

# --- Inlines ---
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ('title', 'status')
    show_change_link = True  # Optional: lets you click to edit full subtask

class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    fields = ('content',)
    readonly_fields = ('created_at',)  # You can't edit created_at
    # Note: 'created_at' isn't editable, but you can display it if needed

# --- Admin Classes ---
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name_plural = "Categories"

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority', 'category')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description')
    inlines = [SubTaskInline, NoteInline]  # 👈 This is the key line!

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'parent_task_name')
    list_filter = ('status',)
    search_fields = ('title',)

    def parent_task_name(self, obj):
        return obj.task.title
    parent_task_name.short_description = 'Parent Task'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)