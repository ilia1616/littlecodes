from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100) # it is a STRING and max char is 10
    password = models.CharField(max_length=102) # you HAVE to define max len
    
    def __str__(self):
        return self.name
    
