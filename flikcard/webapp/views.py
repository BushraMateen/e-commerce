from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from webapp.models import products
from webapp.serializers import productSerializer
# Create your views here.


@csrf_exempt
def productApi(request,uniq_id=0):
    if request.method == 'GET':
        product = products.objects.all()
        product_serializer = productSerializer(product,many=True)
        return JsonResponse(product_serializer.data,safe=False)
    elif request.method == 'POST':
        product_data=JSONParser().parse(request)
        product_serializer = productSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added succesfully",safe=False)
        return JsonResponse("failed to add",safe=True)                
    elif  request.method == 'DELETE' :
            Product = products.objects.get(prodcutuniq_id=id)
            Product.delete()
            return JsonResponse("dleted successfully",safe=False)