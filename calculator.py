#https://github.com/Susieruby/lab10-CC-SW
#Partner1: Cheuvront Cason Makail
#Partner2:Song Wenxi
import math
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return a / b
def log(a, b):
    if a <=0 or a==1 or b<=0:
        raise ValueError
    return math.log(b,a)
def exp(a, b):
    return a**b
def square_root(a):
    if a<0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a,b)

