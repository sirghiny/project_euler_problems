"""Test solutions."""

from unittest import TestCase


class TestSolutions(TestCase):
    """Test cases for solutions."""

    def test_sum_of_multiples(self):
        """Test sum of multiples between limits."""
        from solutions._001_sum_multiples import sum_multiples
        expected = 233168
        actual = sum_multiples(0, 1000, 3, 5)
        self.assertEqual(expected, actual)

    def test_sum_even_fibonacci(self):
        """Test sum of even components of a fibonacci series."""
        from solutions._002_sum_even_fibonacci import sum_even_numbers
        expected = 4613732
        actual = sum_even_numbers(1, 2, 4000000)
        self.assertEqual(expected, actual)
