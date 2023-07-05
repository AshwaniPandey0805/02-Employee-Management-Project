from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    age  = models.IntegerField(max_length=10)
    is_active = models.BooleanField(default = False)

    def __str__(self):
        return self.name


