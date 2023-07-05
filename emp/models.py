from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=50)
    address = models.CharField(max_length = 100)
    working  = models.BooleanField(default=True)
    department = models.CharField(max_length = 50)
     
