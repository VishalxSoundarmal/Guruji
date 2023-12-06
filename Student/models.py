from django.db import models

# Create your models here.

class Student_form(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name

