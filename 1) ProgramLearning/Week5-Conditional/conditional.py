hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Pay Rate: ")
r = float(rate)

if h > 40 :
    overtime_rate = r * 1.5
    overtime_hours = h - 40
    gross_pay = (40 * r) + (overtime_hours * overtime_rate)
else :
    gross_pay = (h * r)

print(gross_pay)
