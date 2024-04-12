from calculator import addition 
from calculator import subtraction
from calculator import division

def test_addition():
    assert addition(1, 2) == 3

def test_subtraction():
    assert subtraction(5, 3) == 2

def test_division():
    assert division(6, 2) == 3