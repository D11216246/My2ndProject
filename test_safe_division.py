"""
Unit Tests for Safe Division Calculator
測試程式碼 - 防呆計算機

This module contains comprehensive unit tests for the safe_division function.
Generated using automated testing best practices.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function"""
    
    def test_basic_division(self):
        """Test basic division operation"""
        result = safe_division(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_division_by_zero(self):
        """Test division by zero returns None"""
        result = safe_division(10, 0)
        self.assertIsNone(result)
    
    def test_negative_dividend(self):
        """Test division with negative dividend"""
        result = safe_division(-10, 2)
        self.assertEqual(result, -5.0)
    
    def test_negative_divisor(self):
        """Test division with negative divisor"""
        result = safe_division(10, -2)
        self.assertEqual(result, -5.0)
    
    def test_both_negative(self):
        """Test division with both negative numbers"""
        result = safe_division(-10, -2)
        self.assertEqual(result, 5.0)
    
    def test_zero_dividend(self):
        """Test zero divided by non-zero number"""
        result = safe_division(0, 5)
        self.assertEqual(result, 0.0)
    
    def test_floating_point_numbers(self):
        """Test division with floating point numbers"""
        result = safe_division(7.5, 2.5)
        self.assertEqual(result, 3.0)
    
    def test_result_with_decimal(self):
        """Test division that results in decimal"""
        result = safe_division(7, 3)
        self.assertAlmostEqual(result, 7/3, places=10)
    
    def test_large_numbers(self):
        """Test division with large numbers"""
        result = safe_division(1000000, 1000)
        self.assertEqual(result, 1000.0)
    
    def test_small_numbers(self):
        """Test division with very small numbers"""
        result = safe_division(0.001, 0.1)
        self.assertAlmostEqual(result, 0.01, places=10)
    
    def test_one_as_divisor(self):
        """Test division by one"""
        result = safe_division(42, 1)
        self.assertEqual(result, 42.0)
    
    def test_one_as_dividend(self):
        """Test one divided by any number"""
        result = safe_division(1, 4)
        self.assertEqual(result, 0.25)
    
    def test_integer_inputs(self):
        """Test that function works with integer inputs"""
        result = safe_division(15, 3)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 5.0)
    
    def test_float_inputs(self):
        """Test that function works with float inputs"""
        result = safe_division(15.0, 3.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 5.0)
    
    def test_mixed_inputs(self):
        """Test that function works with mixed int and float inputs"""
        result = safe_division(15, 3.0)
        self.assertEqual(result, 5.0)

class TestSafeDivisionEdgeCases(unittest.TestCase):
    """Test edge cases for the safe_division function"""
    
    def test_zero_divided_by_zero(self):
        """Test zero divided by zero returns None"""
        result = safe_division(0, 0)
        self.assertIsNone(result)
    
    def test_negative_zero_divisor(self):
        """Test division by negative zero"""
        result = safe_division(10, -0.0)
        self.assertIsNone(result)
    
    def test_very_small_divisor_not_zero(self):
        """Test division by very small number (not zero)"""
        result = safe_division(1, 0.0000001)
        self.assertIsNotNone(result)
        self.assertEqual(result, 10000000.0)


if __name__ == '__main__':
    unittest.main()
