# Python offers a companion to the division operator called the modulo operator. 
# The modulo operator is indicated by % and gives the remainder of a division calculation. 
# If the number is divisible, then the result of the modulo operator will be 0.

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)

# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)

# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)


# You're trying to divide a group into four teams. All of you count off, and you get number 27.
# 1) Find out your team by computing 27 modulo 4. Save the value to my_team.
# 2) Print out my_team. What number team are you on?
# 3) Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams?
my_team = 27 % 4
print(my_team)
print(0, 1, 2, 3)