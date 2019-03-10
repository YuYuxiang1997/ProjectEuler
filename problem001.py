# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 03:34:54 2019

@author: pengu
"""

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

#sum of arithmetic progression
def sumAP(n):
    return (n*(n+1))/2

#main function
def sum35(k):
    k = k-1
    #sum 3s
    sum3s = 3*sumAP(k//3)
    #sum 5s
    sum5s = 5*sumAP(k//5)
    #sum 15s
    sum15s = 15*sumAP(k//15)
    result = sum3s+sum5s-sum15s
    print(result)
    return result

sum35(1000)
