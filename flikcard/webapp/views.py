from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from webapp.models import products
from webapp.serializers import productsSerializer
# Create your views here.


@csrf_exempt
def productApi(request,id=0):
    

    product = products.objects.get(id=int(id))
    
    if request.method == 'GET':
        #product = products.objects.all()
        product_serializer = productsSerializer(product,many=False)
        return JsonResponse(product_serializer.data,safe=False)
    elif request.method == 'POST':
        product_data=JSONParser().parse(request)
        product_serializer = productsSerializer(data=product_data)
        #print(product_serializer.errors)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added succesfully",safe=False)
        return JsonResponse("failed to add",safe=False) 
    elif request.method == 'PUT':
        product_data=JSONParser().parse(request)
        product_serializer = productsSerializer(product,data=product_data)
        #print(product_serializer.errors)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("updated succesfully",safe=False)
        return JsonResponse("failed to update",safe=False)               
    elif  request.method == 'DELETE' :
            Product = products.objects.get(id=id)
            Product.delete()
            return JsonResponse("deleted successfully",safe=False)



def productallApi(request,id=0):
    if request.method == 'GET':
        product = products.objects.all()
        product_serializer = productsSerializer(product,many=True)
        return JsonResponse(product_serializer.data,safe=False)