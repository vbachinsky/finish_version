# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Sales(models.Model):
    region = models.CharField(null=False, max_length=50)
    country = models.CharField(null=False, max_length=50)
    item_type = models.CharField(null=False, max_length=50)
    sales_channel = models.BooleanField(default=False)
    order_priority = models.CharField(null=False, max_length=2)
    order_date = models.DateField(null=True, blank=True)
    order_id = models.PositiveIntegerField(null=True, blank=True)
    ship_date = models.DateField(null=True, blank=True)
    units_sold = models.PositiveIntegerField(null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=True)
    unit_cost = models.FloatField(null=True, blank=True)
    total_revenue = models.FloatField(null=True, blank=True)
    total_cost = models.FloatField(null=True, blank=True)
    total_profit = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.order_id)
