"""Testing helpers."""
import random
import string
from datetime import datetime
from typing import Sequence

from django.utils.timezone import get_current_timezone

from product_listing.models import Company, Category, Product


def _random_str(string_length=12, only_digits=False) -> str:
    """Generates a random string."""
    letters_and_digits = string.digits
    if not only_digits:
        letters_and_digits = letters_and_digits + string.ascii_letters
    return "".join(random.choice(letters_and_digits) for i in range(string_length))


def _parse_date(date: str) -> datetime:
    """Parses a string to date"""
    time_zone = get_current_timezone()
    return time_zone.localize(datetime.strptime(date, '%m/%d/%Y'))


def create_dummy_company(uuid: int, name: str = _random_str()) -> Company:
    """Create a dummy company for testing."""
    company = Company.objects.create(id=uuid, name=name, logo="")
    return company


def create_dummy_category(uuid: int, name: str = _random_str()) -> Category:
    """Create a dummy category for testing."""
    if name == "":
        raise Exception
    category = Category.objects.create(id=uuid, name=name)
    return category


def create_dummy_product(uuid: int, company: Company, categories: Sequence[Category],
                         school: int, price: float, end_date: str,
                         name: str = _random_str()) -> Product:
    """Create a dummy product for testing."""
    product = Product.objects.create(id=uuid, name=name, description="",
                                     photo="", school_type=school,
                                     company=company, price=price,
                                     end_date=_parse_date(end_date))

    return _add_categories_to_product(product=product, categories=categories)


def _add_categories_to_product(product: Product, categories: Sequence[Category]) -> Product:
    """add categories to a product."""
    product.refresh_from_db()
    for category in categories:
        product.categories.add(category)
        product.save()

    return product
