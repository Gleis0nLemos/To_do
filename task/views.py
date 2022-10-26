from ctypes.wintypes import HACCEL
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task

def taskList(request):
    tasks = Task.objects.all()
    return render(request, 'task/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/task.html', {'task': task})

def helloWord(request):
    return HttpResponse('Hello Word!')

def yourName(request, name):
    return render(request, 'task/yourname.html', {'name': name})