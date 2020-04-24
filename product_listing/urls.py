"""This module contains the routing urls"""
from django.conf.urls import url
from django.views.generic import RedirectView

from product_listing.views.category_views import CategoryListView, SingleCategoryView
from product_listing.views.company_views import CompanyListView, SingleCompanyView
from product_listing.views.product_views import ProductListView, SingleProductView

urlpatterns = [
    # Redirect to products/
    url(r'^$', RedirectView.as_view(pattern_name='list_products', permanent=False)),

    # Product Urls.
    url(r'^products/$', ProductListView.as_view(), name="list_products"),
    url(r'^product/(?P<pk>[0-9]+)/$', SingleProductView.as_view(), name='details_product'),

    # Product Filtering Urls.
    url(r'^categories/', CategoryListView.as_view(), name="list_categories"),
    # Gets the products of a category.
    url(r'^category/(?P<pk>[0-9]+)/$', SingleCategoryView.as_view(), name='category_products'),

    url(r'^companies/', CompanyListView.as_view(), name="list_companies"),
    # Gets the products of a company.
    url(r'^company/(?P<pk>[0-9]+)/$', SingleCompanyView.as_view(), name='company_products'),
]
