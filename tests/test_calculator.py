'''My Calculator Test'''
from calculator.calculator_section import Calculations

def test_addition():
    '''Test that addition function works '''    
    assert Calculations.addition(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert Calculations.subtraction(2,2) == 0

def test_multiplication():
    '''Test that multplication function works '''
    assert Calculations.multiplication(3,3) == 9

def test_division():
    '''Test that division function works '''
    assert Calculations.division(9, 3) == 3
