# If we try and run this code it will throw out a NameError.
# Because special_item has only been defined within the scope 
# of the functino create_special_string.
def create_special_string(special_item):
    return "Our special is " + special_item + "."
# Since the above function will not work the print statement has been commented out.
# print("I don't like " + special_item)


current_year = 2048
def calculate_age(birth_year):
  age = current_year - birth_year
  return age
# calculate_age will work fine because current_year
# has been defined outside the function. Therefore
# will work globally within the file. Note that
# the variable has to be defined BEFORE defining
# the function.
print(calculate_age(1970))
