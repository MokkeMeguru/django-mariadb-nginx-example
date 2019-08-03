from rest_framework.serializers import ModelSerializer
from draft_todo.models.user import User
from draft_todo.models.todoItem import TodoItem
from draft_todo.models.authUser import AuthUser
from draft_todo.models.todoItemAsAuth import TodoItemAsAuth
from rest_framework import serializers


class TaskUserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email']


class TaskTodoItemCreateSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['owner', 'todo_name', 'todo_text', 'dead_line']


class TaskTodoItemListSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['owner', 'todo_name', 'todo_text', 'dead_line', 'raise_date']


class TaskAuthUserSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'password']


class TaskAuthAsAuthUserCreateSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='authuser.username')

    class Meta:
        model = TodoItemAsAuth
        fields = ['owner', 'todo_name', 'todo_text', 'dead_line']
