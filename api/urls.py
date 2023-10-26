from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_customer_details_viewset, get_product_viewset, get_sale_viewset
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'customerdetails', get_customer_details_viewset())
router.register(r'product', get_product_viewset())
router.register(r'sale', get_sale_viewset())

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/login/', auth_views.LoginView.as_view(), name='rest_login'),
    path('customer-details/', views.CustomerDetailsList.as_view(), name='customer-details-list'),
    path('customer-details/<int:pk>/', views.CustomerDetailsDetail.as_view(), name='customer-details-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('sales/', views.SaleList.as_view(), name='sale-list'),
    path('sales/<int:pk>/', views.SaleDetail.as_view(), name='sale-detail'),
]

