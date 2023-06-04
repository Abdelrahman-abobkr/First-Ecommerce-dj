from django.shortcuts import render
from .models import *
# Create your views here.



def home(request):
    product = Product.objects.all()
    context = {
        'products':product
    }
    return render(request, 'home.html', context)



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_items': 0, 'get_cart_total': 0}
    context = {
        'items':items,
        'order':order,
    }
    return render(request, 'cart.html', context)



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_items': 0, 'get_cart_total': 0}
    context = {
        'items':items,
        'order':order,
    }
    return render(request, 'checkout.html', context)