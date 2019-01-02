fname = input("Enter File Name: ")
if fname != "mbox-short.txt": fname = "mbox-short.txt"
fhandle = open(fname)

email = dict()
max = 0

for line in fhandle :
    line = line.rstrip()
    if "From" in line :
        words = line.split()
    else :
        continue
    email[words[1]] = email.get(words[1], 0) + 1
    print(email.values())
    # for word in words :
    #     if email[word] > max :
    #         max = email[word]

print(email.keys())
print(max)