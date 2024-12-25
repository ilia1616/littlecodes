from django.db import models

# Create your models here.
class User(models.Model):
    # lookup_field = 'username' #default is id
    username = models.CharField(max_length=10) # it is a STRING and max char is 10
    password = models.CharField(max_length=12) # you HAVE to define max len
    
    def __str__(self):
        return self.username
    
