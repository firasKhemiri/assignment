"""This module contains the Product model."""
import logging
from datetime import datetime

from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.db import models

from product_listing.models import Company
from product_listing.models.category import Category

from product_listing.utils.common_utils import calculate_passed_time


class SchoolType(models.TextChoices):
    """SchoolType choices."""
    praktijkonderwijs = "praktijkonderwijs"
    vmbo = "vmbo"
    mbo = "mbo"
    hbo = "hbo"
    opleidingsbedrijf = "opleidingsbedrijf"

    @classmethod
    def has_value(cls, value):
        """Returns the chosen value."""
        return value in cls.values


class Product(models.Model):
    """The Product model schema."""
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    photo = models.CharField(max_length=250, blank=True, null=True)

    categories = models.ManyToManyField(Category, related_name="products", blank=False)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE,
                                null=False, blank=False, related_name="products")

    school_type = models.CharField(choices=SchoolType.choices,
                                   max_length=200, null=False, blank=False)

    price = models.FloatField(blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    end_date = models.DateTimeField()

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"Product: '{self.__repr__()}'"


    @property
    def categories_count(self):
        """Counts the categories in which the product exist."""
        return self.categories.count()

    @property
    def reached_end_date(self):
        """Checks if product has reached the expiration date."""
        return datetime.now() >= self.end_date

    @property
    def time_passed_since_creation(self):
        """Calculates the elapsed time since creation of the product."""
        return calculate_passed_time(first_date=datetime.now(), second_date=self.date_created)


def categories_changed(sender, **kwargs):
    """Signal on update to check if the number of categories in a product has exceeded six."""
    product = kwargs['instance']
    logging.info(f"{product.name} updated")
    if product.categories.count() > 6:
        raise ValidationError("You can't assign more than six categories")


m2m_changed.connect(categories_changed, sender=Product.categories.through)
