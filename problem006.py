# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 01:25:16 2019

@author: pengu
"""

'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sumsquare(n):
    accum = 0
    for i in range(1,n+1):
        accum += i**2
    print(accum)
    return accum
    
def squaresum(n):
    accum = 0 
    for i in range(1,n+1):
        accum += i
    print(accum)
    return accum**2
    

n = squaresum(100)-sumsquare(100)
print(n)