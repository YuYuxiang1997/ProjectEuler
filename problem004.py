# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 01:10:11 2019

@author: pengu
"""

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#check palindrome
def checkpal(n):
    return str(n) == str(n)[::-1]

#iterate through multiplying 2 numbers
def checknumbers(maxint):
    highest = 0
    for i in range(100,maxint+1):
        for j in range(100,maxint+1):
            if checkpal(i*j):
                highest = max(highest,i*j)
    print(highest)
    return highest


checknumbers(999)