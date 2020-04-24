"""Add models to the admin dashboard."""
from django.contrib import admin
from product_listing.models.category import Category
from product_listing.models.company import Company
from product_listing.models.product import Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Company)
