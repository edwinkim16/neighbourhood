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

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length = 255,null = True)
    full_name = models.CharField(max_length=255, null=True)
    hood = models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)   

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Hood, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=65)