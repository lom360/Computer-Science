def computepay(h, r):
    if h > 40 :
        overtime_hrs = h - 40
        overtime_rate = r * 1.5
        gross_pay = (40 * r) + (overtime_hrs * overtime_rate)
        return gross_pay
    else :
        gross_pay = h * r
        return gross_pay


string_hrs = input("Enter Hours: ")
string_rate = input("Enter pay rate: ")

hrs = int(string_hrs)
rate = float(string_rate)

p = computepay(hrs, rate)
print(p)
