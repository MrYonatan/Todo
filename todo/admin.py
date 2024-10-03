from django.contrib import admin
from .models import TodoItem, TodoList

class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 0
    
class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoItemInline]

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoItem)
