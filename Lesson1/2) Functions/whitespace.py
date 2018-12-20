# When using indentation whether it is 2, 4 or tab spaces.
# it doesn't matter just be consistent.
def greet_customer():
    print("Welcome to Engrossing Grocer's.")
    print("Our special is mandarin oranges.")
    print("Have fun shopping!")
print("Cleanup on Aisle 6")

greet_customer()
# When running the code. Notice that "Cleanup on Aisle 6"
# was printed out first. That is because the greet_customer()
# exist after that line statment. Therefore the leading
# print statement will be called after and print.

# Another example
def about_this_computer():
      print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()