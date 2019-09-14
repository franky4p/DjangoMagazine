"""
Definition of models.
"""

from django.db import models


class Product(models.Model):
    __tablename__ = 'product'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Feature(models.Model):
    __tablename__ = 'feature'
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    product = models.ForeignKey(Product,
                                related_name='feature',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name
