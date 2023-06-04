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
    context = {

    }
    return render(request, 'cart.html', context)



def checkout   (request):
    context = {

    }
    return render(request, 'checkout.html', context)