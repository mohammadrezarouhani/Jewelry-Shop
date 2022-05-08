from django.contrib import admin
from .models import Factor, Product, ProductSold

admin.site.register(Product)
admin.site.register(Factor)
admin.site.register(ProductSold)