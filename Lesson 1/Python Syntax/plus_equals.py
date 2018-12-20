# Python offers a shorthand for updating variables. 
# When you have a number saved in a variable and want 
# to add to the current value of the variable, you can use the += (plus-equals) operator.

# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14


# The plus-equals operator also can be used for string concatenation, like so:
hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

# Problem 1:
# We're doing a little bit of online shopping and find a pair of new sneakers. 
# Right before we check out, we spot a nice sweater and some fun books we also want to purchase!
# Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.
# The prices (also included in the workspace) are:
# new_sneakers = 50.00
# nice_sweater = 39.00
# fun_books = 20.00

total_price = 0
new_sneakers = 50.00
total_price += new_sneakers
nice_sweater = 39.00
fun_books = 20.00

# Update total_price here:
total_price += nice_sweater
total_price += fun_books

print("The total price is", total_price)
