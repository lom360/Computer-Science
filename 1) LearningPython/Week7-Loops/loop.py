largest = None
smallest = None

# Finds largest value
def findMax() :
    global largest
    if largest is None :
        largest = int_val
    elif largest < int_val :
        largest = int_val

# Finds smallest value
def findMin() :
    global smallest
    if smallest is None :
        smallest = int_val
    elif smallest > int_val :
        smallest = int_val

while True:
    str_val = input("Enter a number: ")
    if str_val == "done":
        break
    try :
        int_val = int(str_val) 
    except: 
        print("Invalid input")
        continue
    findMax()
    findMin()  

print("Maximum is", largest)
print("Minimum is", smallest)