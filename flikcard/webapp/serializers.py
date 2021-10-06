from django.db.models import fields
from rest_framework import serializers
from webapp.models import products

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'