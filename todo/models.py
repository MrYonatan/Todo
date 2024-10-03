from django.db import models
from django.contrib.auth import get_user_model

class TodoList(models.Model):
    
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=300,blank=True, null=True)
    created_by = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE,
        related_name='todo_lists',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('created_by', 'name')
    
    def __str__(self):
        return self.name
    
    
    
class TodoItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=300, blank=True, null=True)
    
    created_by = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE,
        related_name='todo_items',
    )
    
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=10, choices= {
            'pending' : 'pending',
            'completed': 'completed'
        }, 
        default = 'pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todo_list = models.ForeignKey(
        TodoList,
        on_delete = models.CASCADE,
    )
    
    class Meta:
        unique_together = ('todo_list', 'name')
    
    def __str__(self):
        return self.name
    