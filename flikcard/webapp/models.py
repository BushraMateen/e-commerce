from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=10000,default=None,blank=True,null=True)
    price = models.CharField(max_length=10000,default=None,blank=True,null=True)
    description = models.CharField(max_length=10000,default=None,blank=True,null=True)
    category = models.CharField(max_length=10000,default=None,blank=True,null=True)
    image = models.CharField(max_length=10000,default=None,blank=True,null=True)
    rate = models.CharField(max_length=10000,default=None,blank=True,null=True)
    count = models.CharField(max_length=10000,default=None,blank=True,null=True)

