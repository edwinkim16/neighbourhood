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

    class Meta:
        ordering = ['-pk']

    def save_hood(self):
        self.save()


    def delete_hood(self):
        self.delete()

    def find_neighborhood(id): 
     '''Method to find neighborhood object instance'''
     neighborhood = Hood.objects.filter(id=id)
     if neighborhood: 
      return neighborhood
    
    def update_neighborhood(self,id): 
     '''Method to update neighborhood object instance'''
     neighborhood = Hood.objects.filter(id=id)
     if neighborhood:
      neighborhood.update(name=self.name,location=self.location) 
    
    def update_occupants(self,id): 
     '''Method to update neighborhood object instance population'''
     neighborhood = Hood.objects.filter(id=id)
     if neighborhood: 
      neighborhood.update(population = self.population)    

    @classmethod
    def search_hood(cls, search_term):
        hood = Hood.objects.filter(name__icontains=search_term)
        return hood


    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length = 255,null = True)
    full_name = models.CharField(max_length=255, null=True)
    hood = models.ForeignKey(Hood,null=True,on_delete=models.CASCADE)   

    def __str__(self):
        return self.full_name

    def save_profile(self):
        self.save()

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_category(cls, category):
        biz = cls.objects.filter(category__name__icontains=category)
        return biz

    @classmethod
    def search_business(cls, search_term):
        business = Business.objects.filter(business_name__icontains=search_term)
        return business


    @classmethod
    def get_business(cls, id):
        business = Business.objects.filter(hood__pk=id)
        return business

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Hood, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    @classmethod
    def get_post(cls, id):
        post = Post.objects.filter(hood__pk=id)
        return post