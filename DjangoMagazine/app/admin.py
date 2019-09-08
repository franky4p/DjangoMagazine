from django.contrib import admin

from .models import Feature, Product

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')

admin.site.register(Product)
