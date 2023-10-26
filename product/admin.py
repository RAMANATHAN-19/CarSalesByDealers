# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_cost', 'product_type', 'product_company', 'product_stock')
    list_filter = ('product_type', 'product_company')
    search_fields = ('product_name', 'product_type', 'product_company')
    ordering = ('product_id',)

admin.site.register(product, ProductAdmin)
