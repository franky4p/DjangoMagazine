"""
Definition of views admin tables.
"""

from django.contrib import admin
from .models import Feature, Product


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'value')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
