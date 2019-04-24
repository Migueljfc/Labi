import pytest
import math
from unitarios import soma,subtracao
import random
def test_soma():
    a = round(random.random(), 14)
    b = round(random.random(), 14)
    c = round(random.random(), 14)
    print("Propriedade distribuitiva")
    assert soma(a,b)==soma(b,a)
    assert soma(a,c)==soma(c,a)
    assert soma(b,c)==soma(c,b)
    print("Propriedade 2")
    

    
'''def test_subtracao():
    a = random(1,100)
    b = random(1,100)
    assert subtracao(a,b)=a+b'''
