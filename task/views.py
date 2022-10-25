from ctypes.wintypes import HACCEL
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def helloWord(request):
    return HttpResponse('Hello Word!')