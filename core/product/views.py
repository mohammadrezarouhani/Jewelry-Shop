from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        param = self.request.query_params.get('user', '')
        if param:
            return Product.objects.filter(user=param)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FactorList:
    pass


class FactorDetail:
    pass


class DailyProfit:
    pass


class MonthlyProfit:
    pass


class CurrencyInfo:
    pass
