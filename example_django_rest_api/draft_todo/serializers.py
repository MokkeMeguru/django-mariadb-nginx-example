from rest_framework.serializers import ModelSerializer
from draft_todo.models import User, TodoItem


class TaskUserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'email']


class TaskTodoItemCreateSerializer(ModelSerializer):
    class Meta:
        model = TodoItem
        fields = [
            'owner',
            'todo_name',
            'todo_text',
            'dead_line'
        ]
