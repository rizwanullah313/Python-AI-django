from attr import define
from django.db import models

# Create your models here.
# Create Models
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    des = models.TextField()
    date = models.DateField()


    def __str__(self) :
        return self.name