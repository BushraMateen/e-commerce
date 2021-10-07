from django.db.models import fields
from rest_framework import serializers
from webapp.models import products

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  products
        fields= ('product_name','retail_price', 'discounted_price','image','description','product_rating','overall_rating','brand')
