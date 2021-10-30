from django.contrib import admin
from .models import Hood, Profile, Business, Post,Location,Category

# Register your models here.
admin.site.register(Hood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)