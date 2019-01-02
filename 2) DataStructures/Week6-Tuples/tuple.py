fname = input("Enter File Name: ")
if fname != "mbox-short.txt" : fname = "mbox-short.txt"

fhandle = open(fname)

hour = dict()

for line in fhandle : 
    line = line.rstrip()
    words = line.split()
    if "From" in words and len(words) == 7 :
        word = words[5]
        numbers = word.split(':')
        for key in numbers :
            hour[key[0]] = hour.get(key[0], 0) + 1
print(hour.items())