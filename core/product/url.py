from django.urls import path
from .views import DailySale, FactorDetail, FactorList, MonthlySale, ProductList,ProductDetail,CurrencyInfo


urlpatterns = [
    path('list/',ProductList.as_view(),name='product-list'),
    path('detail/<str:pk>/',ProductDetail.as_view(),name='product-detail'),
    path('factor/list/',FactorList.as_view(),name='factor-list'),
    path('factor/detail/<str:pk>/',FactorDetail.as_view(),name='factor-list'),
    path('currency/info/',CurrencyInfo.as_view(),name='currency-info'),
    path('daily/sale/',DailySale.as_view(),name='currency-info'),
    path('monthly/sale/',MonthlySale.as_view(),name='currency-info'),
]
