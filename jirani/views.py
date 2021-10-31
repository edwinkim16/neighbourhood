from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from . forms import *
from .models import Hood, Profile, Business, Post,Location
from django.contrib.auth.models import User
from django.contrib import messages

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

def profile(request, username):

    profile = User.objects.get(username=username)
    print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        pass
    user = request.user
    profile = User.objects.get(username=username)
    title = f'@{profile.username} '

    return render(request, 'profile.html', locals()) 

def upload_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            hood.owner= current_user
            upload.save()
            return redirect('home')
    else:
        form = HoodForm()
    return render(request, 'upload_hood.html', locals())