from rest_framework import viewsets,generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Sum
from datetime import date, timedelta
from .currency_prices import get_currency_prices
from . import serializer,models


class ProdcutViewset(viewsets.ModelViewSet):
    serializer_class=serializer.ProductSerializer
    queryset=models.Product.objects.all()
    permissions = [IsAuthenticated]

    
    def get_queryset(self):
        user_id = self.request.query_params.get('user', '')
        query_set=super().get_queryset()
       
        if user_id:
            return query_set.filter(user=user_id)
        
        return query_set


class FactorViewset(viewsets.ModelViewSet):
    serializer_class = serializer.FactorSerializer
    queryset=models.Factor.objects.all()
    permissions = [IsAuthenticated]
    
    def get_queryset(self):
        seller = self.request.query_params.get('seller', '')
        query_set=super().get_queryset()
        if seller:
            return query_set.filter(seller=seller)
        return query_set
    
        



class DailySale(generics.ListAPIView):
    permissions = [IsAuthenticated]
    serializer_class = serializer.DailyPriceSerializer

    def get_queryset(self):
        dt_range = date.today()-timedelta(days=30)
        query = Factor.objects.filter(Q(seller=self.kwargs['user']) & Q(date__gte=dt_range)).values(
            'date').order_by('date').annotate(daily_sale=Sum('total_price'))
        return query


class MonthlySale(generics.ListAPIView):
    permissions = [IsAuthenticated]
    serializer_class = serializer.MonthlyPriceSerializer

    def get_queryset(self):
        dt_range = date.today()-timedelta(days=365)
        query = Factor.objects.filter(Q(seller=self.kwargs['user']) & Q(date__gte=dt_range)).values(
            'date__month','date__year').order_by('date__month').annotate(daily_sale=Sum('total_price'))
        return query


class CurrencyInfo(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = get_currency_prices()
        return Response({'currency': data}, status=status.HTTP_200_OK)
