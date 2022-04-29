from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserRegister,UserDetail

urlpatterns=[
    path('register/',UserRegister.as_view(),name='uer-register'),
    path('detail/<str:pk>/',UserDetail.as_view(),name='user-detail'),
]