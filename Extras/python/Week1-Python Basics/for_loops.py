# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:24:05 2017

@author: Lom
In this file we are given values that will
be printed. Our goal is to convert the printed 
values into codes of "for loops".
"""

"""Problem 1
print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
"""Answer 1:"""
for num in range(2,11,2):
    print(num)
    if num == 10:
        print("Goodbye!")

"""Problem 2
prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""
"""Answer 2:"""
print('\n')
for num in range(10,0,-2):
    if num == 10:
        print("Hello!")
    print(num)

"""Problem 3
Write a while loop that sums the values 1 
through end, inclusive. end will be a variable
already assigned a value. So an example is if 
we define end to be 6, your code should print out
the result: 21
which is 1 + 2 + 3 + 4 + 5 + 6.
"""
print('\n')
end = 6
sum = 0
for num in range(1,end+1):
    sum = sum + num
print(sum)