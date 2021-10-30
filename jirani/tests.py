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

class HoodTestClass(TestCase):
    def setUp(self):
        self.tao =Hood(name='tao',location='survey',occupants=5)
        # self.my_hood.save()

    def tearDown(self):
        Hood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.tao,Hood))

    def test_save_hood(self):
        self.tao.save_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(Hood)>0)