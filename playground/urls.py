# in this module we're gonna map our urls to view functions.
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/',views.say_hello,name='hello'),
    path('customer/',views.random_query,name='customer'),
    path('order/',views.average_payment_status,name ='order' )
]