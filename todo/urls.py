from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('update/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
