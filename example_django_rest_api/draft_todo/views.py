from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from draft_todo.models.user import User
from draft_todo.models.todoItem import TodoItem
from draft_todo.serializers import (TaskUserCreateSerializer,
                                    TaskTodoItemCreateSerializer,
                                    TaskTodoItemListSerializer)
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.viewsets import ModelViewSet
from draft_todo.models.authUser import AuthUser
from draft_todo.serializers import TaskAuthUserSerializer

from draft_todo.models.todoItemAsAuth import TodoItemAsAuth
from draft_todo.serializers import TaskAuthAsAuthUserCreateSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

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


class TaskAuthUserAPIView(ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = TaskAuthUserSerializer


class TaskAuthUserCreateTodoItemAPIView(LoginRequiredMixin, CreateAPIView):
    queryset = TodoItemAsAuth.objects.all()
    serializer_class = TaskAuthAsAuthUserCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
