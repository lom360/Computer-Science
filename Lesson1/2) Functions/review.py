# 12/20/2018
# Review Problem
# 1) Define a function called repeat_stuff that takes in two inputs, stuff, and num_repeats. 
#    We will want to make this function print a string with stuff repeated num_repeats amount of times. 
#    For now, only put an empty print statement inside the function.
# 2) Outside of the function, call repeat_stuff.
#    You can use the value "Row " for stuff and 3 for num_repeats.
# 3) Change the print statement inside repeat_stuff to a return statement instead.
#    It should return stuff*num_repeats.
#    Note: Multiplying a string just makes a new string with the old one repeated! 
#    For example: "na"*6 results in the string "nananananana".
# 4) Give the parameter num_repeats a default value of 10.
# 5) Add repeat_stuff("Row ", 3) and the string "Your Boat. " together and save the result to a variable called lyrics.
# 6) Create a variable called song and assign it the value of repeat_stuff called with the singular input lyrics.
# 7) Print song. Good job!
def repeat_stuff(stuff, num_repeats=10):
    return stuff*num_repeats
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)
print(song)
