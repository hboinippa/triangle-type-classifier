import pytest


def classifyTriangle(a, b, c):
    """

    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'


    """
    # Note: This code is completely bogus but demonstrates a few features of python
    if a == b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isoceles'
    elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
        return 'Right'
    elif a != b and a != c and b != c:
        return 'Scalene'
    else:
        return 'NotATriangle'



