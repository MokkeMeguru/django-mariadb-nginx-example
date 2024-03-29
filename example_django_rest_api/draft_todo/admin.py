from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.todoItem import TodoItem
from .models.authUser import AuthUser
from .models.todoItemAsAuth import TodoItemAsAuth
from django.contrib.auth.admin import UserAdmin

admin.site.register(User)
admin.site.register(TodoItem)
admin.site.register(TodoItemAsAuth)
admin.site.register(AuthUser, UserAdmin)
