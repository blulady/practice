# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 10:22:37 2021

@author: ssang
"""

def sum(n,m):

    for num in range(n,1,-1):
        if n % num == 0 and m % num == 0:
            print(num)
            quotent1 = n/num
            print(quotent1)
            quotent2 = m/num
            return(quotent1 + quotent2)
        
        
def sum2(n,m):

    for num in range(n,0,-1):
        if n % num == 0 and m % num == 0:
            print(num)
            quotent1 = n/num
            print(quotent1)
            quotent2 = m/num
            return(quotent1 + quotent2)
        