from django.db import models

# Create your models here.
class Categories(models.Model):
    category= models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Subcategories(models.Model):
    subcategory= models.CharField(max_length=50)
    category= models.ForeignKey(Categories, related_name="categories",  on_delete = models.CASCADE)
    def __str__(self):
        return self.subcategory

class Product(models.Model):
    product= models.CharField(max_length=50)
    subcategory= models.ForeignKey(Subcategories, related_name="subcategories", on_delete = models.CASCADE)


