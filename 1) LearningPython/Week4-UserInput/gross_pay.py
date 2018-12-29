# This first line is provided for you

hrs = input("Enter Hours: ")
rate = input("Enter Pay Rate: ")

# float() converts string or int into a float type.
gross_pay = float(hrs) * float(rate)
print("Pay:", gross_pay)
