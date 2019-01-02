fname = input("Enter File Name: ")
if fname != "mbox-short.txt" : fname = "mbox-short.txt"
fhandle = open(fname)

hour = dict()
temp = list()

for line in fhandle : 
    line = line.rstrip()
    words = line.split()
    if "From" in words and len(words) == 7 :
        word = words[5]
        number = word.split(':')
        hour[number[0]] = hour.get(number[0], 0) + 1

for k,v in hour.items() :
    temp.append((k,v))

temp = sorted(temp)
for key, val in temp :
    print(key, val)