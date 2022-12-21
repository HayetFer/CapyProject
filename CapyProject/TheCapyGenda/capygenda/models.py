from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Diary(models.Model):
    db_table=input
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Todo(models.Model):
    text=models.CharField(max_length=100)
    complete=models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.text