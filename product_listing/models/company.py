"""This module contains the Company model"""
from django.db import models


class Company(models.Model):
    """The Company model schema"""
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=250)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"Company: '{self.__repr__()}'"
