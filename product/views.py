import pdb
from rest_framework import generics,status
from rest_framework.views import APIView
from .models import Factor, Product
from .serializer import FactorSerializer, ProductSerializer
from .currency_prices import get_currency_prices
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permissions=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        param = self.request.query_params.get('user', '')
        if param:
            return Product.objects.filter(user=param)

  
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permissions=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class FactorList(generics.ListCreateAPIView):
    serializer_class=FactorSerializer
    permissions=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    

    def get_queryset(self):
        param=self.request.query_params.get('seller','')
        if param:
            return Factor.objects.filter(seller=param)


class FactorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=FactorSerializer
    queryset=Factor.objects.all()
    permissions=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]



class DailySale(APIView):
    permissions=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request,foramt=None):
        pass


class MonthlySale(APIView):
    permissions=[IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request,foramat=None):
        pass


class CurrencyInfo(generics.ListAPIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,format=None):
        data=get_currency_prices()
        return Response({'currency':data},status=status.HTTP_200_OK)
