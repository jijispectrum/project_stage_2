from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('product/', views.product, name='product'),
    path('upload/', views.upload_product, name='upload_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
