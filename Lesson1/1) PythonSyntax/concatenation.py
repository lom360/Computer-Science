# The + operator doesn't just add two numbers, it can also "add" two strings! 
# The process of combining two strings is called string concatenation.

greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"
print(full_text)

# let's add the space in-between using the same concatenation operator!
full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)


# If you want to concatenate a string with a number you will need to make 
# the number a string first, using the str() function. If you're trying to 
# print() a numeric variable you can use commas to pass it as a different 
# argument rather than converting it to a string.
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If we just want to print an integer
# we can pass a variable as an argument to
# print() regardless of whether
# it is a string.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

# More practice
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

print(message)
