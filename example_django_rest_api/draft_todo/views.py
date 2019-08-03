from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from draft_todo.models import User, TodoItem
from draft_todo.serializers import (TaskUserCreateSerializer,
                                    TaskTodoItemCreateSerializer,
                                    TaskTodoItemListSerializer)
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class TaskUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = TaskUserCreateSerializer


class TaskTodoItemCreateAPIView(CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TaskTodoItemCreateSerializer


class TaskTodoItemListAPIView(ListAPIView):
    # queryset = TodoItem.objects.all()
    serializer_class = TaskTodoItemListSerializer

    def get_queryset(self):
        owner = self.kwargs['owner']
        return TodoItem.objects.filter(owner=owner)


class TaskTodoItemRetrieveAPIView(RetrieveAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TaskTodoItemListSerializer
