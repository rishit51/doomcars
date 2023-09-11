# Create your models here.
from django.db import models
import uuid
# Create your models here.
class Car(models.Model):
    id=models.UUIDField(default=uuid.uuid3,primary_key=True,unique=True,blank=False)