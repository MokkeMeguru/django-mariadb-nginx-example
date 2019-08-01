from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from draft_todo.models import User
from draft_todo.serializers import TaskUserCreateSerializer, TaskTodoItemCreateSerializer
# Create your views here.


class TaskUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TaskUserCreateSerializer
