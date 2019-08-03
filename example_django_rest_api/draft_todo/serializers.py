from rest_framework.serializers import ModelSerializer
from draft_todo.models.user import User
from draft_todo.models.todoItem import TodoItem


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
