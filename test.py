from main import *

def test_hello():
    assert hello() == 'Hello FastAPI'

def test_isPrime():
    assert is_prime(13)==True

def test_fibonacci():
    assert fibonacci(3)==2