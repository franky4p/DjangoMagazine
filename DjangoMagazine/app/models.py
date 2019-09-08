"""
Definition of models.
"""

from django.db import models

class Product(models.Model):
    __tablename__ = 'product'
    name = models.CharField(max_length=100)


class Feature(models.Model):
    __tablename__ = 'feature'
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
