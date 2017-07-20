# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    cost = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=255)
