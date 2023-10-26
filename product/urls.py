from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login"),
    path('product-record', views.productlisting, name="productlisting"),
    path('product-add', views.add, name="add"),
    path('update/<str:productId>/', views.update, name="update"),
    path('delete/<str:id>/', views.delete, name="delete"),
]

