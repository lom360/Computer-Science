hrs = input("Enter Hours: ")
rate = input("Enter Pay Rate: ")
# Coverting string input to int.
try :
    h = float(hrs)
    r = float(rate)
except :
    print("There has been an issue. Quiting program.")
    quit()

# If worked over 40 hours will calculate overtime pay.
if h > 40 :
    # Up to 40hrs will be paid normal rate
    # Extra hours will increase by 1.5
    overtime_rate = r * 1.5
    overtime_hours = h - 40
    gross_pay = (40 * r) + (overtime_hours * overtime_rate)
else :
    gross_pay = (h * r)

print(gross_pay)