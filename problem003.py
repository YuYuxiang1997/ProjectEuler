# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 03:50:37 2019

@author: pengu
"""

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import floor,sqrt

#get list of prime numbers
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

def primefac(n,primes):
    maxfac = 1
    while n not in primes:
        for prime in primes:
            if n%prime == 0:
                print(prime)
                maxfac = prime
                n = n//prime
    print(maxfac)
    return maxfac
        

primes = getprimes(floor(sqrt(600851475143)))
print("primes generated")
primefac(600851475143,primes)