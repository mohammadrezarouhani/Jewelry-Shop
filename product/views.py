import pdb
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Factor, FactorProduct, Product
from .serializer import (
    DailyPriceSerializer,
    FactorSerializer,
    MonthlyPriceSerializer,
    ProductSerializer
)
from .currency_prices import get_currency_prices
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta
from django.db.models import Q, Sum


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permissions = [IsAuthenticated]

    def get_queryset(self):
        param = self.request.query_params.get('user', '')
        if param:
            return Product.objects.filter(user=param)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permissions = [IsAuthenticated]


class FactorList(generics.ListCreateAPIView):
    serializer_class = FactorSerializer
    permissions = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        total_price=sum(i['price']-i['tax']-i['discount'] for i in request.data['product_sold'])
        request.data['total_price']=total_price
        return super().create(request,*args,**kwargs)
        

    def get_queryset(self):
        param = self.request.query_params.get('seller', '')
        if param:
            return Factor.objects.filter(seller=param)


class FactorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FactorSerializer
    queryset = Factor.objects.all()
    permissions = [IsAuthenticated]


class DailySale(generics.ListAPIView):
    permissions = [IsAuthenticated]
    serializer_class = DailyPriceSerializer

    def get_queryset(self):
        dt_range = date.today()-timedelta(days=30)
        query = Factor.objects.filter(Q(seller=self.kwargs['user']) & Q(date__gte=dt_range)).values(
            'date').order_by('date').annotate(daily_sale=Sum('total_price'))
        return query


class MonthlySale(generics.ListAPIView):
    permissions = [IsAuthenticated]
    serializer_class = MonthlyPriceSerializer

    def get_queryset(self):
        query = """
            select 1 id,
            sum(cast(total_price as int )) - sum(cast(tax as int)) - sum(cast (discount as int)) as price ,
            to_char(date,'Mon') as month,
            extract(year from date) as year
            from products_factor 
            where extract(month from DATE(date))  > extract(month from DATE(CURRENT_DATE)) - 12
            and products_factor.seller_id = %s
            group by 3,4
        """
        return Factor.objects.raw(query, [self.kwargs['user']])


class CurrencyInfo(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = get_currency_prices()
        return Response({'currency': data}, status=status.HTTP_200_OK)
