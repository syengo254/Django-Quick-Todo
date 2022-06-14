from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {"todos": todos}

    return render(request, 'todolist/base.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()

    return redirect('todolist:index')


@require_http_methods(["POST"])
def add_todo(request):
    title = request.POST.get('title')
    todo = Todo(title=title)
    todo.save()

    return redirect('todolist:index')


@require_http_methods(["GET"])
def del_todo(request, pk):
    Todo.objects.get(pk=pk).delete()

    return redirect('todolist:index')