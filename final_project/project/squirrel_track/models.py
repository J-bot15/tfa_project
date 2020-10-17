from django.db import models

# Create your models here.
class Squirrel(models.Model):
    x=models.CharField(max_length=100)
    y=models.CharField(max_length=100)
    Unique_Squirrel_ID=models.CharField(max_length=100)
    Shift=(('A','AM'),('P','PM'))
    Date=models.DateField(<auto_now=false, **options="" auto_now_add="True,">)
    Age=(('A','Adult'),('J','Juvenile'))
