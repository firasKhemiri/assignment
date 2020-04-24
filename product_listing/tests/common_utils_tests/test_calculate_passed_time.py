"""Test different scenarios for the elapsed time calculating function."""
from datetime import datetime

from django.test import TestCase

from product_listing.exceptions import InvalidDate
from product_listing.utils.common_utils import calculate_passed_time


class ElapsedTimeTest(TestCase):
    """Test elapsed time between two dates"""

    def test_elpased_time_days(self):
        """1 day difference."""
        second = datetime(2020, 3, 5, 23, 8, 15)
        first = datetime(2020, 3, 6, 23, 8, 15)

        time = calculate_passed_time(first_date=first, second_date=second)
        self.assertEqual(time, "1 days ago")

    def test_elpased_time_hour(self):
        """1h59 difference."""
        first = datetime(2020, 3, 6, 22, 15, 15)
        second = datetime(2020, 3, 6, 20, 16, 15)

        time = calculate_passed_time(first_date=first, second_date=second)
        self.assertEqual(time, "1 hours ago")

    def test_elpased_time_two_hours(self):
        """2 hours difference."""
        first = datetime(2020, 3, 6, 22, 16, 15)
        second = datetime(2020, 3, 6, 20, 16, 15)

        time = calculate_passed_time(first_date=first, second_date=second)
        self.assertEqual(time, "2 hours ago")

    def test_elpased_time_minutes(self):
        """10 minutes difference."""
        first = datetime(2020, 3, 6, 22, 18, 15)
        second = datetime(2020, 3, 6, 22, 8, 15)

        time = calculate_passed_time(first_date=first, second_date=second)
        self.assertEqual(time, "10 minutes ago")

    def test_invalid(self):
        """Invalid date comparison."""
        first = datetime(2020, 2, 6, 20, 18, 15)
        second = datetime(2020, 3, 6, 22, 8, 15)
        with self.assertRaises(InvalidDate):
            calculate_passed_time(first_date=first, second_date=second)
