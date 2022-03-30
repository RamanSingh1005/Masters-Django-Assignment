from rest_framework import serializers
from webp.models import Categories
from webp.models import Subcategories
from webp.models import Product

# class CategoriesSerializer(serializers.ModelSerializer):
#     categories=SubcategoriesSerializer(many=True)
#     class Meta:
#         model=Categories
#         fields= ('id', 'category', 'subcategories')

class SubcategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Subcategories
        fields= '__all__'
        
class CategoriesSerializer(serializers.ModelSerializer):
    categories=SubcategoriesSerializer(many=True)
    class Meta:
        model=Categories
        fields= ('id', 'category', 'categories')

class CategoriesSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model=Categories
        fields= ('id', 'category')



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields= '__all__'

class SubcategoriesSerializer1(serializers.ModelSerializer):
    product= ProductSerializer(many=True)
    class Meta:
        model=Subcategories
        fields= ('id', 'subacategory', 'product')

class CategoriesSerializer2(serializers.ModelSerializer):
    categories=SubcategoriesSerializer(many=True)
    product= ProductSerializer(many=True)
    class Meta:
        model=Categories
        fields= ('id', 'categories', 'product')