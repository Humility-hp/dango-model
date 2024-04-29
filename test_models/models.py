from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
 nomenclature = models.CharField(max_length=30)
 notes = models.CharField(max_length=30)

class Client(models.Model):
 team = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
 name = models.CharField(max_length=255)
 created_at = models.DateTimeField(auto_now_add=True)
 changed_at = models.DateTimeField(auto_now=True)