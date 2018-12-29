# Use the file name mbox-short.txt as the file name
count = 0
total = 0
average = 0
fname = input("Enter file name: ")

while(fname != "done") :
    try :
        fh = open(fname)
        break
    except :
        print("Invalid file")
        fname = input("Enter file name: ")
        continue

for line in fh :
    if "X-DSPAM-Confidence:" in line:
        # ipos = line.find("0")
        # num = float(line[ipos : ])
        # The two commented line above is equivalent to the line below this.
        num = float(line[line.find("0") : ])
        count = count + 1
        total = total + num

# Averaging the number and rounding to the 12th decimal place.
average = round(total/count, 12)
print("Average spam confidence:", average)