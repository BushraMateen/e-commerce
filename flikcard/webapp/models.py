from django.db import models

# Create your models here.
class products(models.Model):
    product_name = models.CharField(max_length=10000,default=None,blank=True,null=True)
    retail_price = models.CharField(max_length=10000,default=None,blank=True,null=True)
    discounted_price = models.CharField(max_length=10000,default=None,blank=True,null=True)
    image = models.CharField(max_length=10000,default=None,blank=True,null=True)
    description = models.CharField(max_length=10000,default=None,blank=True,null=True)
    product_rating = models.CharField(max_length=100,default=None,blank=True,null=True)
    overall_rating = models.CharField(max_length=100,default=None,blank=True,null=True)
    brand = models.CharField(max_length=100,default=None,blank=True,null=True) 
