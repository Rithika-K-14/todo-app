from django.urls import path
from . import views
app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todolistView, name='todo'),
    path('addTodoItem/',views.addTodoView), 
    path('deleteTodoItem/<int:i>/', views.deleteTodoView), 
] 