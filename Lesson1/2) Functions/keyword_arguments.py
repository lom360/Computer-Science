# Whichever value is put into greet_customer() first is assigned to grocery_store, 
# and whichever value is put in second is assigned to special_item. These are 
# called positional arguments because their assignments depend on their positions in the function call.
# def greet_customer(grocery_store, special_item):
#     print("Welcome to " + grocery_store + ".")
#     print("Our special is " + special_item + ".")
#     print("Have fun shopping!")


# We can also pass these arguments as keyword arguments, where we explicitly refer to what each argument 
# is assigned to in the function call.
def greet_customer(special_item, grocery_store="Engrossing Grocer's"):
    print("Welcome to " + grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")

# In this case, grocery_store has a default value of "Engrossing Grocer's". If we call the function with 
# only one argument, the value of "Engrossing Grocer's" is used for grocery_store:
greet_customer("bannas")

# Example Problem
# Define create_spreadsheet():
def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called " + title +
        " with " + str(row_count) + " rows.")


# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)
