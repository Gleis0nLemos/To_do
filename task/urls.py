from django.urls import path
from . import views

urlpatterns = [
    path('Helloword/', views.helloWord),
    path('', views.taskList, name='Task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]
