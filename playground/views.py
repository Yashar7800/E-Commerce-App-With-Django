from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# a view function is a function that takes a request and returns response
# more accurately is a request handler
# action
from store.models import Product
from store.models import Customer
from store.models import *
# Every model in Django has an attribute called objects and this returns a manager object which is an interface to the database. The methods from the object return a query set 

from django.core.exceptions import ObjectDoesNotExist # we add this library of django couldnt find the proper result, like .get(pk = 0) --> since we dont have pk = 0


def say_hello(request):
    
    queryset = Product.objects.filter(title__istartswith = 'wine').filter(last_update__year = 2020)
    for product in queryset:
        print(product)

    query_customer = Customer.objects.filter(email__iendswith = '.com').filter(first_name__istartswith = 'n')
    for customer in query_customer:
        print(customer)

    query_collection = Collection.objects.filter(featured_product_id__isnull = True)
    for collection in query_collection:
        print(collection)
    query_inventory = Product.objects.filter(inventory__lt= 10)
    for product in query_inventory:
        print(product)
    query_order = Order.objects.filter(customer_id = 1)
    for order in query_order:
        print(order)

    return render(request, 'hello.html',{'name':'Yashar', 'products': list(queryset), 'customers': list(query_customer),'collections': list(query_collection),
                                         'Inventory_less_than_10': list(query_inventory),'orders': query_order})

# we need to map this view to a url, so when we get a request at that url the function is called.

