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
from django.db.models import Q # we add this class for writing queries
from django.db.models import F # Using this class we can reference a particular field
from django.db.models import Avg, Value
from django.db.models.functions import Coalesce





def say_hello(request):
    
    queryset = Product.objects.filter(Q(title__istartswith = 'wine') | ~Q(last_update__year = 2020)).order_by('unit_price', '-title').reverse()[3:20].values('title','unit_price','collection__title')
    # queryset = Product.objects.filter(inventory = F('collection_id'))
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

def random_query(request):
    queryset= Customer.objects.raw("SELECT C.id,concat_ws(' ', first_name, last_name) as Full_Name, payment_status FROM storefront.store_customers as C inner join storefront.store_order as O on C.id = O.customer_id where payment_status = 'C';")

    return render(request, 'customer.html', {'title': 'Customers Query Page','customers':list(queryset)})

def average_payment_status(request):

    queryset = OrderItem.objects.annotate(
        total_price=F('quantity') * F('unit_price')  # Calculate quantity * unit_price
    ).values(
        'order__payment_status'  # Group by payment_status from related Order
    ).annotate(
        AVG_PaymentStatus=Avg('total_price')  # Calculate average for each group
    ).order_by('AVG_PaymentStatus')  # Order by the calculated average

    return render(request, 'order.html',{'title': 'Average Order Price for payment Status','avg_orders': list(queryset)})
