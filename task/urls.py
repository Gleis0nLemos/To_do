from django.urls import path
from . import views

urlpatterns = [
    path('Helloword/', views.helloWord),
]
