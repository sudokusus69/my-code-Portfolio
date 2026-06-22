import numpy as np 
from numpy import random


def random_randint():
    x =  random.randint(100, size=(3,2))
    for row in x:
        for y in row:
            if y % 10 == 0:
                print(y)
            else:
                print("no number found with matching condition")
                break

def random_choice():
    x = random.choice([1, 2, 3, 4, 5], size=(3,2))
    print(x)



