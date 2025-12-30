from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# a view function is a function that takes a request and returns response
# more accurately is a request handler
# action

def say_hello(request):

    return render(request, 'hello.html',{'name':'Yashar'})

# we need to map this view to a url, so when we get a request at that url the function is called.

