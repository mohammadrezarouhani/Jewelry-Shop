from django.urls import path
from .views import UserRegister,UserDetail,PasswordReset
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

urlpatterns=[
    path('register/',UserRegister.as_view(),name='user-register'),
    path('detail/<str:pk>/',UserDetail.as_view(),name='user-detail'),
    path('password-change/<str:pk>/',PasswordReset.as_view(),name='password-forget'),
    path('token-obtain/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('token-refresh/',TokenRefreshView.as_view(),name='token-refresh'),
]