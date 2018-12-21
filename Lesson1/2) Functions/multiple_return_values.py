# Sometimes we may want to return more than one value from a function. 
# We can return several values by separating them with a comma:
def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2

# This function takes in an x value and a y value, 
# and returns them both, squared. We can get those 
# values by assigning them both to variables when we 
# call the function:
x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)

# Practice Problem
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
low, high = get_boundaries(100, 20)
print("Low limit: " + str(low)  + ", high limit: " + str(high))