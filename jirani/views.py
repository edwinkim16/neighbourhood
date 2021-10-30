from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Hood, Profile, Business, Post,Location

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    hoods = Hood.objects.all()
    return render(request,'home.html',locals())    