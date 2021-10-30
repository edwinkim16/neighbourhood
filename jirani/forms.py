from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hood, Profile, Business, Post,Location

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ['name', 'location','image',]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]