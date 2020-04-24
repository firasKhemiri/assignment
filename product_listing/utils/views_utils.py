"""This module contains functions are necessary for the views"""
from datetime import datetime, timezone
from typing import Sequence

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from product_listing.constants import Constants
from product_listing.exceptions import IndexOutOfBound
from product_listing.models import Product, Company, Category


def get_category_products(category: Category) -> Sequence[Product]:
    """Retrieve the non expired products of a certain category."""
    products = Product.objects.filter(Q(categories__in=[category])
                                      & Q(end_date__gt=datetime.now(tz=timezone.utc)))
    return products


def get_company_products(company: Company) -> Sequence[Product]:
    """Retrieve the non expired products of a certain company."""
    products = Product.objects.filter(Q(company=company)
                                      & Q(end_date__gt=datetime.now(tz=timezone.utc)))
    return products


def paginate_products(products, page: int, elements_count) -> Sequence[Product]:
    """Divide received products into multiple page of products if possible."""
    paginator = Paginator(products, elements_count)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return products


def order_products(products, ordering: int) -> Sequence[Product]:
    """Return the list of products with a different ordering."""
    if ordering == Constants.ALPHA_ASC:
        products = products.order_by('name')
    elif ordering == Constants.ALPHA_DES:
        products = products.order_by('name').reverse()

    elif ordering == Constants.DATE_ASC:
        products = products.order_by('date_created').reverse()
    elif ordering == Constants.DATE_DES:
        products = products.order_by('date_created')

    elif ordering == Constants.PRICE_ASC:
        products = products.order_by('price')
    elif ordering == Constants.PRICE_DES:
        products = products.order_by('price').reverse()
    else:
        raise IndexOutOfBound()

    return products
