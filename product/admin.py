from django.contrib import admin
from .models import Factor, Product, FactorProduct

admin.site.register(Product)
admin.site.register(Factor)
admin.site.register(FactorProduct)