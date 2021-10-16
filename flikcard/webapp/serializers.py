from django.db.models import fields
from rest_framework import serializers
from webapp.models import products

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  products
        fields= ('title','price', 'description','category','image','rate','count')


