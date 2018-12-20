# We can make a function take more than one parameter by using commas:
def greet_customer(grocery_store, special_item):
    print("Welcome to " + grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")

# The variables grocery_store and special_item must now both be provided to the function upon calling it:
greet_customer("Stu's Supplies", "papayas")

# Practice example
def mult_x_add_y(number, x, y):
    print(number*x + y)

mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)