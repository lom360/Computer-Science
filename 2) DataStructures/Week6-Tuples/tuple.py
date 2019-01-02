fname = input("Enter File Name: ")
if fname != "mbox-short.txt" : fname = "mbox-short.txt"

fhandle = open(fname)

hour = dict()
lst = list()

for line in fhandle : 
    line = line.rstrip()
    words = line.split()
    if "From" in words and len(words) == 7 :
        word = words[5]
        number = word.split(':')
        hour[number[0]] = hour.get(number[0], 0) + 1
            
