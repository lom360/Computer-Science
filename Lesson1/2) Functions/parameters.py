# In the definition heading for greet_customer(), the special_item is referred to as 
# a formal parameter. This variable name is a placeholder for the name of the item 
# that is the grocery's special today. Now, when we call greet_customer, we have to provide a special_item:
def greet_customer(special_item):
    print("Welcome to Engrossing Grocer's.")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
# The value between the parentheses when we call the function (in this case, "peanut butter") 
# is referred to as an argument of the function call. The argument is the information that is 
# to be used in the execution of the function. When we then call the function, Python assigns 
# the formal parameter name special_item with the actual parameter data, "peanut_butter". 
# In other words, it is as if this line was included at the top of the function:
greet_customer("peanut butter")

# Another example
def mult_two_add_three(number):
  print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three(1)
mult_two_add_three(5)
mult_two_add_three(-1)
mult_two_add_three(0)
