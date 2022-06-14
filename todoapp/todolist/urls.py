from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_todo, name="add-todo"),
    path('update/<int:pk>/', views.update_todo, name="update-todo"),
    path('del/<int:pk>/', views.del_todo, name="del-todo"),
]