from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.todoItem import TodoItem
from .models.authUser import AuthUser


admin.site.register(User, TodoItem, AuthUser)
# admin.site.register(TodoItem)
# admin.site.register(AuthUser)
