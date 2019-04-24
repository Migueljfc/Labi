import pytest
from fibonacci import fibonacci
import random

def test_inferior_1():
    print("Testa comportamento com n < 1")
    assert fibonacci(0) == []
    assert fibonacci(-1) == []
def test_fibonacci_1():
    print("Testa comportamento com n=1")
    assert fibonacci(1)==[0,1]
def test_fibonacci_2():
    print("Testa comportamento com n=2")
    assert fibonacci(2) == [0,1,1]
def test_fibonacci_5():
    print("Testa comportamento com n=5")
    assert fibonacci(5)==[0,1,1,2,3,5]
def test_fibonacci_n():
    print("Testa comportamento com qq n")
    n=random.randint(10,100)
    assert len(fibonacci(n)) == n+1
