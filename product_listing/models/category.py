"""This module contains the Category model"""
from django.db import models


class Category(models.Model):
    """The Category model schema"""
    name = models.CharField(max_length=50)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"Category: '{self.__repr__()}'"
