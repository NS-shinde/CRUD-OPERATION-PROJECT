from django.db import models


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    address = models.TextField()
    phone = models.IntegerField()
    
    def __str__(self) -> str:
        return (self.name)