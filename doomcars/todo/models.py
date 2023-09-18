from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    title=models.CharField(max_length=40)
    task=models.TextField()
    completed=models.BooleanField(default=False)
