from django.db import models

class student(models.Model):
    Id= models.CharField(max_length=100)
    Name= models.CharField(max_length=50)
    course= models.CharField(max_length=50)
    
    publication_date = models.DateField()

    def __str__(self):
        return self.title