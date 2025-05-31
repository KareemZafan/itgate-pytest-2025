 
import math


def add(x, y): 
    return x + y 


def sub(x, y): 
    return x - y 


def mul(x, y): 
    return x * y 


def div(x, y): 
    try:
        return x / y
    except ZeroDivisionError: 
        return None


def abs(x):
    if(x >= 0 ): 
        return x 
    else: 
        return x * -1


def get_square_root(a):
    return math.sqrt(a)
    


