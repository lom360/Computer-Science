num = 0
total = 0.0

# Loop will always run until user enters 'done'
# Otherwise loop will ask user to input a number.
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try: 
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    num = num + 1
    total = total + fval

print("Total:", total, " Number:", num," Average:", total/num)