from django.contrib import admin
from .models import Categories
from .models import Subcategories
from .models import Product

# Register your models here.

admin.site.register(Categories)
admin.site.register(Subcategories)
admin.site.register(Product)