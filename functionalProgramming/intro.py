#principles

# - Imnutability :values should't be modified once created
# - Pure functions: Function behavior is always predictable
# - Referential Transparency: Functios with same imput have same output
# - First order functions: Function wich allow taking other functions as arguments


#Help to catch errors not cover in unit tests

#type systems implementation
#A way to add constraints to your code

def add_(x: int, y:int) -> int:  #proposition
    return x + y                #proof


#Functional programming
from typing import Callable

x = ...

def sort(method: Callable): #same as using @abstract decorator that asked you to have sort method from parent class in all son classes
    method(x)


