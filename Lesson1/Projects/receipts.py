# Date: 12/19/2018
# Project 1
# Create Purchasing Information and Receipts for Lovely Loveseats

# We've decided to pursue the dream of small-business ownership 
# and open up a furniture store called Lovely Loveseats for Neat Suites 
# on Fleet Street. With our newfound knowledge of Python programming, 
# we're going to build a system to help speed up the process of creating 
# receipts for your customers.

# In this project, we will be storing the names and prices of a furniture 
# store's catalog in variables. You will then process the total price and 
# item list of customers, printing them to the output terminal.

# Please note: Projects do not run tests against your code. This experience 
# is more open to your interpretation and gives you the freedom to explore. 
# Remember that all variables must be declared before they are referenced in your code.

#loveseat
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00

#settee
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50

#lamp
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15

#Sales tax
sales_tax = .088

#We are initializing customer 1 with total purchase cost to 0 and description of items to an empty string
customer_one_total = 0
customer_one_itemization = ""

#Customer 1 is purchasing two items so we are adding up the total and description.
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#Here we are calculating tax for customer one.
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

#Printing out customer 1 receipt
print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(customer_one_total)

#Creating second customer
customer_two_total = 0
customer_two_itemization = ""

#Adding up price of items and creating description
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

#Calculating sales tax for customer
customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

#Printing out customer 2 receipt
print("Customer Two Items: ")
print(customer_two_itemization)
print("Customer Two Total: ")
print(customer_two_total)

# Note that there are of course better ways to implement this receipt system.
# However we are ONLY applying the lessons we have learned from Python Syntax.