from django.contrib import admin
from .models import CustomerDetails  # Import the CustomerDetails model

@admin.register(CustomerDetails)
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'CustomerName', 'Carcompany', 'car_type', 'PhoneNumber')
    list_filter = ('Carcompany', 'car_type')
    search_fields = ('CustomerName', 'PhoneNumber')


