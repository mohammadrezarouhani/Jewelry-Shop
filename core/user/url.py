from django.urls import path
from .views import UserRegister,UserDetail,PasswordReset

urlpatterns=[
    path('register/',UserRegister.as_view(),name='uer-register'),
    path('detail/<str:pk>/',UserDetail.as_view(),name='user-detail'),
    path('password-change/<str:pk>/',PasswordReset.as_view(),name='password-forget'),
]