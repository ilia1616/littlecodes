from django.db import models

# Create your models here.
class User(models.Model):
    # lookup_field = 'username' #default is id
    id = models.IntegerField(primary_key=True)
    # category = models.CharField(max_length=10) # it is a STRING and max char is 10
    # name = models.CharField(max_length=12) # you HAVE to define max len
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=15)
    
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'goods'
    
