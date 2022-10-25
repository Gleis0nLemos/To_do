from django.urls import path
from . import views

urlpatterns = [
    path('Helloword/', views.helloWord),
    path('', views.taskList, name='Task-list'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
