"""This module's purpose is to simplify calculations related to triangles."""
import math
__author__ = "Ethan Acevedo"
__version__ = "1.0"

def hypotenuse(s1, s2):
    """This function calculates the hypotenuse given the legs of a right triangle"""
    return math.sqrt(s1**2 + s2**2)

def area(s1, s2):
    """This function calculates the area of a right triangle given its width and height"""
    return (s1*s2)/2

