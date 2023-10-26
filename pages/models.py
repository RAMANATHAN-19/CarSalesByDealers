# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    sr_no = models.PositiveIntegerField()
    CustomerName = models.CharField(max_length=100)
    Carcompany = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    PhoneNumber = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.CustomerName

    class Meta:
        app_label = 'pages'

