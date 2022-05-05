from django.urls import path
from .views import ProductList,ProductDetail

urlpatterns = [
    path('list/',ProductList.as_view(),name='product-list'),
    path('detail/<str:pk>/',ProductDetail.as_view(),name='product-detail'),
]
