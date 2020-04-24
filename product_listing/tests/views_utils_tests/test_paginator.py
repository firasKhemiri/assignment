"""Test different scenarios of product pagination."""
from django.test import TestCase

from product_listing.models import Product
from product_listing.tests.test_setup import test_setup
from product_listing.utils.views_utils import paginate_products


class ProductPaginatorTest(TestCase):
    """Test product count with different pagination parameters"""
    def setUp(self):
        test_setup()

    def test_valid_page_product_count(self):
        """This should only return 1 as there are 4 products and a page only shows 3."""
        products = Product.objects.all()
        products = paginate_products(products=products, page=2, elements_count=3)
        self.assertEqual(len(products), 1)

    def test_non_valid_page_product_count(self):
        """This should only return 1 as the paginator retrieves the last page
        if the given page is not valid."""
        products = Product.objects.all()
        products = paginate_products(products=products, page=3, elements_count=3)
        self.assertEqual(len(products), 1)

    def test_non_int_page_product_count(self):
        """This should only return 1 as the paginator retrieves the last page
        if the given page is not an integer."""
        products = Product.objects.all()
        products = paginate_products(products=products, page="4", elements_count=3)
        self.assertEqual(len(products), 1)
