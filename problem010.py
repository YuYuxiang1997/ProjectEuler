# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 01:47:13 2019

@author: pengu
"""
from math import floor,sqrt


def getprimes(max):
    def check_prime(n):
        threshold = floor(sqrt(n))
        for i in range(2,threshold+1):
            if n%i == 0:
                return False
        return True
    primes = []
    for i in range(2,max+1):
        if check_prime(i):
            primes.append(i)
    return primes

print(sum(getprimes(2000000)))