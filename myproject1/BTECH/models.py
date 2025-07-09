from django.db import models

class student(models.Model):
    id = models.CharField(max_length=100)
    name= models.CharField(max_length=50)
    course= models.CharField(max_length=50)
    publication_date = models.DateField()

    def __str__(self):
        return self.title