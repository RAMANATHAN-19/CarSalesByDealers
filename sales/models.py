# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class sales(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_car_name = models.CharField(max_length=255, default="", unique=True)
    order_customer_name = models.CharField(max_length=255, default="")
    order_date = models.CharField(max_length=255, default="")
    order_cars = models.CharField(max_length=255, default="")


    def __str__(self):
        return self.order_customer_name

