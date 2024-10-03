from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import TodoItem, TodoList
from .forms import TodoListForm, TodoItemForm
from django.contrib.auth.decorators import login_required


class TodoListsView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = 'todo/todo_lists.html'
    context_object_name = 'todo_lists'

    def get_queryset(self):
        return TodoList.objects.filter(created_by=self.request.user)

class TodoItemsView(LoginRequiredMixin, DetailView):
    model = TodoList
    template_name = 'todo/todo_items.html'
    context_object_name = 'todo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_items'] = TodoItem.objects.filter(todo_list=self.object)
        return context


@login_required(login_url='/users/login')
def home_view(request):
    todo_lists = TodoList.objects.filter(created_by=request.user)
    return render(request, 'todo/home.html', {'todo_lists': todo_lists})

class CreateTodoListView(CreateView):
    form_class = TodoListForm
    template_name = 'todo/create_todo_list.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("home")

class CreateTodoItemView(CreateView):
    form_class = TodoItemForm
    template_name = 'todo/create_todo_item.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.todo_list_id = self.kwargs['todo_list_id']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("todo_items", args=[self.kwargs['todo_list_id']])

class UpdateTodoListView(UpdateView):
    model = TodoList
    form_class = TodoListForm
    template_name = 'todo/update_todo_list.html'

    def get_queryset(self):
        return TodoList.objects.filter(created_by=self.request.user)

    def get_success_url(self):
        return reverse("home")

class UpdateTodoItemView(UpdateView):
    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todo/update_todo_item.html'

    def get_queryset(self):
        return TodoItem.objects.filter(created_by=self.request.user)

    def get_success_url(self):
        return reverse("todo_items", args=[self.object.todo_list.id])

class DeleteTodoListView(DeleteView):
    model = TodoList
    template_name = 'todo/delete_todo_list.html'

    def get_queryset(self):
        return TodoList.objects.filter(created_by=self.request.user)

    def get_success_url(self):
        return reverse("home")

class DeleteTodoItemView(DeleteView):
    model = TodoItem
    template_name = 'todo/delete_todo_item.html'

    def get_queryset(self):
        return TodoItem.objects.filter(created_by=self.request.user)

    def get_success_url(self):
        return reverse("todo_items", args=[self.object.todo_list.id])

class TodoItemDetailView(DetailView):
    model = TodoItem
    template_name = 'todo/todo_item_detail.html'

    def get_queryset(self):
        return TodoItem.objects.filter(created_by=self.request.user)

    def get_success_url(self):
        todo_list = self.object.todo_list
        return reverse("todo_items", args=[todo_list.id])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_item'] = self.object
        return context
    
