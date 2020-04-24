"""Test different scenarios retrieving a company products."""
from django.test import TestCase

from product_listing.models import Company
from product_listing.tests.test_setup import test_setup
from product_listing.utils.views_utils import get_company_products


class GetCompanyProductsTest(TestCase):
    """Test the product count of different companies."""
    def setUp(self):
        test_setup()

    # Company 1 has 2 products.
    def test_get_company_products(self):
        """Test an existing company product count."""
        company = Company.objects.get(id=1)
        products = get_company_products(company)
        self.assertEqual(len(products), 2)

    def test_get_non_existent_company_products(self):
        """Test a non existing company product count."""
        with self.assertRaises(Exception):
            company = Company.objects.get(id=5)
            get_company_products(company)

    def test_get_company_has_no_products(self):
        """Test an empty company product count."""
        company = Company.objects.get(id=1)
        products = get_company_products(company)
        self.assertEqual(len(products), 2)
