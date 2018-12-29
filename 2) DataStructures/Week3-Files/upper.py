fname = input("Enter file name: ")

try :
    fh = open(fname)
except :
    print("File does not exist")
    quit()

for line in fh :
    uppercase_line = line.rstrip().upper()
    print(uppercase_line)
