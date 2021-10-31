from django.shortcuts import render, redirect
from django.http  import HttpResponse
from .models import Hood, Profile, Business, Post,Location

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    hoods = Hood.objects.all()
    return render(request,'home.html',locals())    

def hood(request,hood_id):
    current_user = request.user
    hood_name = current_user.profile.hood
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    businesses = Business.get_business(hood_id)
    posts = Post.get_post(hood_id)

    return render(request,'hood.html',locals())    