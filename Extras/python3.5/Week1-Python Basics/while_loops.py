# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 20:51:32 2017

@author: Lom

In this file we are given values that will
be printed. Our goal is to convert the printed 
values into codes of "while loops".
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
num1 = 2
while num1 <= 100:
    if num1 > 10:
        print("Goodbye!")
        break
    print(num1)
    num1 += 2


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
num2 = 10
while num2 >= 2:
    if num2 == 10:
        print("Hello!")
    print(num2)
    num2 -= 2

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
while end >= 1:
    sum = sum + end
    end -= 1
print(sum)
