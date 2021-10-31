from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #url('^$',views.welcome,name = 'welcome'),
    url(r'^$', views.home, name='home'),
    url(r'^hood/(?P<hood_id>\d+)', views.hood, name='hood'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/', views.upload_hood, name='upload'),
    url(r'^join(?P<hood_id>\d+)', views.join, name='join'),
    url(r'^leave/(?P<hood_id>\d+)', views.leave, name='leave')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)