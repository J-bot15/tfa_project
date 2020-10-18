from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Squirrel(models.Model):
    x=models.CharField(max_length=100)
    y=models.CharField(max_length=100)
    Unique_Squirrel_ID=models.CharField(max_length=100)
    Shift=models.CharField(max_length=100)
    Date=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
