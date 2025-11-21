"""
Safe Division Calculator - Project Zero
防呆計算機

This module provides a safe division function that prevents division by zero errors.
"""


def safe_division(a, b):
    """
    Safely divides two numbers and prevents division by zero errors.
    
    Args:
        a (float or int): The dividend (numerator)
        b (float or int): The divisor (denominator)
    
    Returns:
        float: The result of a / b if b is not zero
        None: If b is zero (division by zero would occur)
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(7, 3)
        2.3333333333333335
        >>> safe_division(-10, 2)
        -5.0
    """
    if b == 0:
        return None
    return a / b
