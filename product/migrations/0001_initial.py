# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-10-24 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=255, unique=True)),
                ('product_cost', models.CharField(default='', max_length=20)),
                ('product_type', models.CharField(default='', max_length=255)),
                ('product_company', models.CharField(default='', max_length=255)),
                ('product_stock', models.CharField(default='', max_length=255)),
            ],
        ),
    ]