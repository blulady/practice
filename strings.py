# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:37:14 2021

@author: ssang
"""
#longest substring = beggh
s = 'azcbobobegghakl'

longest = ''
tempstr = ''
for L in range(len(s)-1):
    if s[L] > s[L+1]:
        tempstr += s[L]
print(tempstr)
    