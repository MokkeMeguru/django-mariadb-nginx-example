from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
# from .models.myuser import MyUser
from .models  import MyUser

admin.site.register(MyUser, UserAdmin)
