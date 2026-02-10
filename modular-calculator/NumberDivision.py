"""
Division Module
This module provides a function for performing division.
"""

# Function Name: PerformDivision
# Description: Divides first number by the second number.
# Parameters:
#     a (float) - Numerator
#     b (float) - Denominator (must not be zero)
# Return:
#     float - Result of division
# Raises:
#     ValueError - If denominator is zero
def PerformDivision(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
