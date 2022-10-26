from ctypes.wintypes import HACCEL
from http.client import HTTPResponse
from unicodedata import name
from venv import create
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'task/addtask.html', {'form': form})

def helloWord(request):
    return HttpResponse('Hello Word!')

def yourName(request, name):
    return render(request, 'task/yourname.html', {'name': name})