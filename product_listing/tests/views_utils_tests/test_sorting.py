"""Test different product sorting scenarios."""
from django.test import TestCase

from product_listing.models import Product
from product_listing.tests.test_setup import test_setup
from product_listing.utils.views_utils import order_products


class ProductSortingTest(TestCase):
    """Test if products are sorted correctly."""
    def setUp(self):
        test_setup()

    def test_name_sorting_asc(self):
        """Sort products alphabetically ascending."""
        products = Product.objects.all()
        products = order_products(products=products, ordering=1)
        self.assertEqual(products[0].name, "a")

    def test_name_sorting_desc(self):
        """Sort products alphabetically descending."""
        products = Product.objects.all()
        products = order_products(products=products, ordering=2)
        self.assertEqual(products[0].name, "d")

    def test_price_sorting_asc(self):
        """Sort products by price ascending."""
        products = Product.objects.all()
        products = order_products(products=products, ordering=5)
        self.assertEqual(products[0].price, 25)

    def test_price_sorting_desc(self):
        """Sort products by price descending."""
        products = Product.objects.all()
        products = order_products(products=products, ordering=6)
        self.assertEqual(products[0].price, 250)
