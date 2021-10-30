from django.test import TestCase
from .models import Hood, Profile, Business, Post,Location
from django.contrib.auth.models import User

# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.tao =Location(name='tao',locations='survey')
        

    def test_instance(self):
        self.assertTrue(isinstance(self.tao,Location))    

    def test_save_loc(self):
        self.tao.save_loc()
        looc = Location.objects.all()
        self.assertTrue(len(Location)>0)    

