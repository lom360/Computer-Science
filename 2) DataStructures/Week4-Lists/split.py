fname = input("Enter file name: ")
fh = open(fname)

lst = list(fh)
for line in lst:
    print(line.rstrip())
