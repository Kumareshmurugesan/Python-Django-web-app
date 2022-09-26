from django.db import models
from django.contrib.auth.models import User
import os
import datetime

def getFileName(requset,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-Show,1-Hidden')
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False) 
    actual_price=models.FloatField(null=False,blank=False) 
    selling_price=models.FloatField(null=False,blank=False) 
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0-Show,1-Hidden')
    trending=models.BooleanField(default=False,help_text='0-Default,1-Trending')
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name        







