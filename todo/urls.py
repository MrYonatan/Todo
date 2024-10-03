from django.urls import path
from . import views

urlpatterns = [
    
    path('create_todo_list/', views.CreateTodoListView.as_view(), name='create_todo_list'),
    path('todo_lists/<int:todo_list_id>/create_todo_item/', views.CreateTodoItemView.as_view(), name='create_todo_item'),
    path('todo_lists/<int:pk>/update/', views.UpdateTodoListView.as_view(), name='update_todo_list'),
    path('todo_lists/<int:pk>/delete/', views.DeleteTodoListView.as_view(), name='delete_todo_list'),
    path('todo_lists/<pk>/', views.TodoItemsView.as_view(), name='todo_items'),
    path('todo_items/<int:pk>/update/', views.UpdateTodoItemView.as_view(), name='update_todo_item'),
    path('todo_items/<int:pk>/delete/', views.DeleteTodoItemView.as_view(), name='delete_todo_item'),
    path('todo_items/<int:pk>/detail/', views.TodoItemDetailView.as_view(), name='todo_item_detail'),
    
]
