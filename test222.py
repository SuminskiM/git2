from functions import *

def test_add():
    assert add(3, 5) == 8
    assert add(120, 54) == 174

def test_multiply():
    assert multiply(100, 5) == 500
    assert multiply(100, 1.1) == 110