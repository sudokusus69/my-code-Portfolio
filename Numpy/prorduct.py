# -*- coding: utf-8 -*-
import numpy as np


# using product in numpy
# product of all elements in a array    

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

def product():
    print(np.multiply(a,b))
    print(np.prod(a))
    print(np.prod([a,b]))  # element-wise multiplication/ product along columns



def lcm_gcd():
    # lcm and gcd of all elements in a array
    # to find the lcm and gcd in numpy
    print(np.lcm.accumulate([a,b]))  # lcm of all elements in a array
    print(np.gcd.reduce([a,b]))  # gcd of all elements in a array

    print(np.lcm.reduce([a,b], axis=0))  # lcm along columns
    print(np.gcd.reduce([a,b], axis=0))  # gcd along columns
    print(np.lcm.reduce([a,b], axis=1))  # lcm along rows
    print(np.gcd.reduce([a,b], axis=1))  # gcd along rows


def lcm_gcd_with_arange():
    # Create an array using np.arange
    # Demonstrating the use of np.arange with lcm and gcd

    arr = np.arange(1, 11)  # Array of integers from 1 to 10
    print("Array:", arr)
    
    # Compute lcm and gcd for the array
    print("LCM of array:", np.lcm.reduce(arr))
    print("GCD of array:", np.gcd.reduce(arr))

lcm_gcd_with_arange()