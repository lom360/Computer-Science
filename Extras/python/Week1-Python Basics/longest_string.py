# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:25:14 2017

@author: Lom
"""

s = 'azcbobobegghakl'

start = 0
end   = 0
tempCount = 1
maxCount  = 1
for i in range(len(s)):
    if s[i] >= s[i-1]:
        if maxCount < tempCount:
            start = end
            
            maxCount  = tempCount
            tempCount = 0
        tempCount =+ 1
        i =+ 1
    else:
        end = i - 1
        maxCount = tempCount
    
print(s[start:end])