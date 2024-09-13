from django.urls import re_path as url
from django.urls import path, include
from .views import (
    ToDoListApiView,
)

urlpatterns = [
    path('todo', ToDoListApiView.as_view()),
]
