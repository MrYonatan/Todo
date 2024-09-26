from django.contrib import admin
from .models import TodoItem, TodoList
from django.contrib.auth.mixins import PermissionRequiredMixin

class TodoListAdmin(PermissionRequiredMixin, admin.ModelAdmin):
    permission_required = 'todo_list.owner'

class TodoItemAdmin(PermissionRequiredMixin, admin.ModelAdmin):
    permission_required = 'todo_item.todo_list.owner'

admin.site.register(TodoList)
admin.site.register(TodoItem)