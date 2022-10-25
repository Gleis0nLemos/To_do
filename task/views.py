from ctypes.wintypes import HACCEL
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

def helloWord(request):
    return HttpResponse('Hello Word!')

def taskList(request):
    return render(request, 'task/list.html')

def yourName(request, name):
    return render(request, 'task/yourname.html', {'name': name})