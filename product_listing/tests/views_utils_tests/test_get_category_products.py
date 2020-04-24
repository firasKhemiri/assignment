"""Test different scenarios retrieving category products."""
from django.test import TestCase

from product_listing.models import Category
from product_listing.tests.test_setup import test_setup
from product_listing.utils.views_utils import get_category_products


class GetCategoryProductsTest(TestCase):
    """Test the product count of different categories."""
    def setUp(self):
        """Setup dummies."""
        test_setup()

    # Category 2 has 3 products.
    def test_get_category_products(self):
        """Test an existing category product count."""
        category = Category.objects.get(id=2)
        products = get_category_products(category)
        self.assertEqual(len(products), 3)

    def test_get_non_existent_category_products(self):
        """Test a non existing category product count."""
        with self.assertRaises(Exception):
            category = Category.objects.get(id=6)
            get_category_products(category)

    def test_get_category_has_no_products(self):
        """Test an empty category product count."""
        category = Category.objects.get(id=5)
        products = get_category_products(category)
        self.assertEqual(len(products), 0)
