from django.urls import path
from .views import DailySale, FactorDetail, FactorList, MonthlySale, ProductList,ProductDetail,CurrencyInfo


urlpatterns = [
    path('list/',ProductList.as_view(),name='product-list'),
    path('detail/<str:pk>/',ProductDetail.as_view(),name='product-detail'),
    path('factor-list/',FactorList.as_view(),name='factor-list'),
    path('factor-detail/<str:pk>/',FactorDetail.as_view(),name='factor-detail'),
    path('daily-sale/<str:user>/',DailySale.as_view(),name='daily-sale'),
    path('monthly-sale/<str:user>/',MonthlySale.as_view(),name='monthly-sale'),
    path('currency-info/',CurrencyInfo.as_view(),name='currency-info'),

]
