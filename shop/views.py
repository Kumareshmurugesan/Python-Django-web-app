from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render, redirect
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login

def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,'shop/index.html',{"products":products}) 
def login_page(request):
      if request.method=="POST":
       name=request.POST.get('username')
       pwd=request.POST.get('password')
       user=authenticate(request,username=name,password=pwd)
      return render(request,'shop/login.html') 
def register(request):
    form=CustomUserForm()
    if request.method=="POST":
      form=CustomUserForm(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request,"Registration Success ")
        return redirect('login')
    return render(request,'shop/register.html',{"form":form})  

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,'shop/collection.html',{"catagory":catagory}) 
def collectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
      products=Product.objects.filter(catagory__name=name)
      return render(request,'shop/products/index.html',{"products":products,'catagory_name':name})
  else:
    messages.warning(request,"No Such catagory found")
    return redirect('collections')  
    

def Product_details(request,cname,pname):     
  if(Catagory.objects.filter(name=cname,status=0)):
   if(Catagory.objects.filter(name=cname,status=0)):
     products=Product.objects.filter(name=pname,status=0).first()
     return render(request,"shop/products/productdetails.html",{"products":products})
   else:
     messages.error(request,"No Such catagory found")
     return redirect('collections')

  else:
     messages.error(request,"No Such catagory found")
     return redirect('collections')   

