# in this module we're gonna map our urls to view functions.
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/',views.say_hello,name='hello'),
]