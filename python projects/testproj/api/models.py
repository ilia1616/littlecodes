from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10) # it is a STRING and max char is 10
    password = models.CharField()
    
    def __str__(self):
        return self.name
    
