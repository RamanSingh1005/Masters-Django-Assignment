from django.urls import path

from . import views

urlpatterns = [
    path('',views.home),
    path('categories',views.get_categories),
    path('subcategories',views.get_subcategories1),
    path('subcategoriesres',views.get_subcategories),
    path('productbysubcategory',views.get_productbysubcategories),
    path('productbycategory',views.get_productbycategories),
    path('allproductsbycategoriesres',views.get_productbycategories2),
    path('allproductsbysubcategoriesres',views.get_productbycategories3),
    
]