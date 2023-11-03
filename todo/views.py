from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    context = {'todos': todos, 'form': form}
    return render(request, 'todo_list.html', context)


def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    context = {'form': form}
    return render(request, 'update_todo.html', context)


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')

    context = {'todo': todo}
    return render(request, 'delete_todo.html', context)
