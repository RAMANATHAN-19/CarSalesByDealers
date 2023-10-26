from django.contrib import admin
from .models import sales  # Import the correct model

@admin.register(sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_car_name', 'order_customer_name', 'order_date','order_cars')

