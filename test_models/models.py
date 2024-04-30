from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Person(models.Model):
 SHIRT_SIZES =(
  ("S","Small"),
  ("M","Medium"),
  ("L","Large"),
 )
 name_shirt = models.CharField("shirts",max_length=30)
 notes = models.CharField(max_length=30)
 shirts = models.CharField(max_length=100, choices=SHIRT_SIZES, default=None, blank=True, null=True)
 selection = models.TextChoices("MedalType","GOLD SILVER BRONZE")

class Publication(models.Model):
 title = models.CharField(max_length=30)
 class Meta:
  ordering = ["title"]
 
 def __str__(self):
  return self.title
 
class Article(models.Model):
 headline = models.CharField("Headlines",max_length=100)
 pulications = models.ManyToManyField(Publication)
 
 class Meta:
  ordering =["headline"]
 
 def __str__(self):
  return self.headline

class MySpecialUser(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 supervisor = models.ManyToManyField(User, related_name="supervisor_of")
 
 def __str__(self):
  return self.user