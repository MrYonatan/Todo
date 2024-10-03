# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from todo.models import TodoItem, TodoList
from .forms import CustomUserCreationForm, CustomUserChangeForm

class TodoListInline(admin.TabularInline):
    model = TodoList
    extra = 0
    fk_name = 'created_by'

class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 0
    fk_name = 'created_by'

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm    
    model = User
    list_display = ['username', 'email', 'is_staff']
    inlines = [TodoListInline, TodoItemInline]

admin.site.register(User, CustomUserAdmin)