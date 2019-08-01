from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=30, validators=[MinLengthValidator(5)], unique=True)
    email = models.EmailField()

    def __str__(self):
        return "{}-{}".format(self.nickname, self.email)

class TodoItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=100)
    todo_text = models.TextField(blank=True, null=True)
    dead_line = models.DateTimeField()
    raise_date = models.DateTimeField(auto_now_add=True)
    importance = models.IntegerField(null=True)
    close_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return "{}-{}".format(self.owner, self.todo_name)

    class Meta:
        ordering = ('dead_line', 'raise_date')
