from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('single/', views.single, name='single'),
]