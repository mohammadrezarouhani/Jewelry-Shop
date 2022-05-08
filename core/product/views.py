from rest_framework import generics
from .models import Factor, Product
from .serializer import FactorSerializer, ProductSerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        param = self.request.query_params.get('user', '')
        if param:
            return Product.objects.filter(user=param)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FactorList(generics.ListCreateAPIView):
    serializer_class=FactorSerializer
    

    def get_queryset(self):
        param=self.request.query_params.get('seller','')
        if param:
            return Factor.objects.filter(seller=param)


class FactorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=FactorSerializer
    queryset=Factor.objects.all()



class DailyProfit:
    pass


class MonthlyProfit:
    pass


class CurrencyInfo:
    pass
