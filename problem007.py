# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 01:28:46 2019

@author: pengu
"""
from math import floor,sqrt

def check_prime(n):
    threshold = floor(sqrt(n))
    for i in range(2,threshold+1):
        if n%i == 0:
            return False
    return True


def make_primes(n):
    primes = [2,3]
    i = 4
    while len(primes)<n:
        if check_prime(i):
            primes.append(i)
        i += 1
    print(primes[n-1])
    return primes[n-1]

make_primes(10001)