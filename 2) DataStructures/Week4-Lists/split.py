fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for line in fh:
    line = line.rstrip() # Eliminates newline
    words = line.split() # Split individual words into an array.
    for word in words :  # Nested loop to check for word duplicates.
        if word in lst :
            continue
        else :
            lst.append(word)

lst.sort()
print(lst)