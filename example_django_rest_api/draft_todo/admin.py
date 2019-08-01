from django.contrib import admin

# Register your models here.
from .models import User, TodoItem

admin.site.register(User)
admin.site.register(TodoItem)
