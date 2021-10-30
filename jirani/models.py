from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    locations = models.CharField(max_length=65)
       
    name = models.CharField(max_length=65)



    def save_loc(self):
        self.save()

    def delete_loc(self):
        self.delete()


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name    
        
class Hood(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image')
    occupants = models.CharField(max_length=50)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, null=True)            