from django.urls import path
from .views import FactorDetail, FactorList, ProductList,ProductDetail

urlpatterns = [
    path('list/',ProductList.as_view(),name='product-list'),
    path('detail/<str:pk>/',ProductDetail.as_view(),name='product-detail'),
    path('factor/list/',FactorList.as_view(),name='factor-list'),
    path('factor/detail/<str:pk>/',FactorDetail.as_view(),name='factor-list'),
]
