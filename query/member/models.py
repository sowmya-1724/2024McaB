from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    firstname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True)
    lastname = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return self.id