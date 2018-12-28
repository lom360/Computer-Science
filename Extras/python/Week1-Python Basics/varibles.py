# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 23:41:28 2017

@author: Lom
"""

varA = 7
varB = "adieu"

if type(varA) == str or type(varB) == str:
    print("string involved")
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    elif varA < varB:
        print("smaller")

varA = 1    
varB = -8

if type(varA) == str or type(varB) == str:
    print("string involved")
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    elif varA < varB:
        print("smaller")