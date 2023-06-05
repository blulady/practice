# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:14:52 2021

@author: ssang
"""
s = "2342341"
def password(s):
    
    for letter in s:
        if letter.islower() == True:
            lowerLetter = True
        else:
            lowerLetter = False
    for letter in s:
        if letter.isupper() == True:
            upperLetter = True
        else:
            upperLetter = False
    for letter in s:
        if letter.isdigit() == True:
            number = True
        else:
            number = False
            
    if number == True and lowerLetter == True and upperLetter == True:
        
        return True
    else:
        return False
    
    
def password2(s):
    for letter in s:
        print(s.find(letter.islower()))