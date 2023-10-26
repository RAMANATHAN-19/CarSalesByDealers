from django.urls import path
from . import views

urlpatterns = [
    path('', views.saleslisting, name="saleslisting"),
    path('add', views.add, name="add"),
    path('delete/<str:id>/', views.delete, name="delete"),
    path('order-details/<str:id>/', views.order_details, name="order_details"),
    path('delete/items/<str:id>/', views.delete_oi, name="delete_oi"),
]


