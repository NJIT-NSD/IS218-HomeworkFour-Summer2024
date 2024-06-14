'''My Calculator Test'''
from calculator import addition, subtraction, multiplication, division

def test_addition():
    '''Test that addition function works '''    
    assert addition(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtraction(2,2) == 0

def test_multiplication():
    '''Test that multplication function works '''
    assert multiplication(3,3) == 9

def test_division():
    '''Test that division function works '''
    assert division(9, 3) == 3

def test_divide_by_zero():
    '''Test that divide by zero error occurs '''
    assert division(5, 0) == 1

#def history_operations():
#    '''Check History'''
