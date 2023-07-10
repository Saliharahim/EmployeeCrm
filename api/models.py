from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=150)
    department=models.CharField(max_length=200)
    salary=models.IntegerField()
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name