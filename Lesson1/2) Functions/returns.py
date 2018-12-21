# So far, we have only seen functions that print out some result to the console. 
# Functions can also return a value to the user so that this value can be modified 
# or used later. When there is a result from a function that can be stored in a 
# variable, it is called a returned function value. We use the keyword return to do this.
def divide_by_four(input_number):
    return input_number/4
result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")

# We can also return strings.
def create_special_string(special_item):
    return "Our special is " + special_item + "."
special_string = create_special_string("banana yogurt")
print(special_string)


# Practice problem
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
my_age = calculate_age(2018, 1993)
dads_age = calculate_age(2018, 1953)
print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")