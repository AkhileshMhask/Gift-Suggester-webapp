import razorpay
from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404
# MOdels Import
from .models import Products
# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,"contactus.html")

def product_detail(request,pk):
    product = get_object_or_404(Products,pk=pk)
    if request.method == "POST":
        amount = int(product.price)
        order_currency = 'INR'
        client = razorpay.Client(auth={'rzp_test_9SK5NWsdqkv2p1','sYFVXMooiFTaA9emnCf6R3NP'})
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,'product_detail.html',context={'product':product})

def get_products(request):
    product = Products.objects.all()
    return render(request,'product_list.html',context={'product':product})

