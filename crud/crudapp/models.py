from django.db import models

# Create your models here.
class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=30)
