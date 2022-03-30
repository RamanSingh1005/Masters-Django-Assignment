from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from webp.models import Categories
from webp.models import Subcategories
from webp.models import Product
from .serializers import *

# Create your views here.

@api_view(['GET'])
def get_categories(request):
    #category
    categories= Categories.objects.all()
    serializer = CategoriesSerializer1(categories, many = True)

    # data = serializer.data
    # new = None
    # print("\n\n\n")
    # for datapoint in data:
    #     if(category == datapoint['category']):
    #       new
    #     print(datapoint)

    # print("\n\n\n")
    # print(category == datapoint['category'])
    # print("\n\n\n")
    return Response(serializer.data)





@api_view(['GET'])
def get_subcategories(request):
    categories= Categories.objects.all()
    serializer = CategoriesSerializer(categories, many = True)
    data=serializer.data

    category=request.GET["category"]

    for d in data:
        if(d['category'] == category):
            corr_id = d['id']-1

    return Response(data[corr_id])

@api_view(['GET'])
def get_productbycategories2(request):
    product = Product.objects.all()
    serializer = CategoriesSerializer2(product, many = True)
    data=serializer.data

    category=request.GET["category"]

    for d in data:
        if(d['category'] == category):
            corr_id = d['id']-1
            break

    return Response(data[corr_id])

@api_view(['GET'])
def get_productbycategories3(request):
    product = Product.objects.all()
    serializer = SubcategoriesSerializer1(product, many = True)
    data=serializer.data

    category=request.GET["category"]

    for d in data:
        if(d['category'] == category):
            corr_id = d['id']-1
            break

    return Response(data[corr_id])


def get_subcategories1(request):
    return render(request,"subcategories.html")


def get_productbysubcategories(request):
    return render(request,"productbysubcategories.html")

def get_productbycategories(request):
    return render(request,"productbycategories.html")

def home(request):
    return render(request,"home.html")

