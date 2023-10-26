# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class CustomerDetails(models.Model):
    sr_no = models.PositiveIntegerField()
    CustomerName = models.CharField(max_length=100)
    Carcompany = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    PhoneNumber = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.CustomerName

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, default="")
    product_cost = models.CharField(max_length=20, default="")
    product_type = models.CharField(max_length=255, default="")
    product_company = models.CharField(max_length=255, default="")
    product_stock = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.product_name

class Sale(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_car_name = models.CharField(max_length=255, default="", unique=True)
    order_customer_name = models.CharField(max_length=255, default="")
    order_date = models.CharField(max_length=255, default="")
    order_cars = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.order_customer_name
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

