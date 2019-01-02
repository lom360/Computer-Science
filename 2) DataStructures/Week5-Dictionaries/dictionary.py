fname = input("Enter File Name: ")
if fname != "mbox-short.txt": fname = "mbox-short.txt"
fhandle = open(fname)

email = dict()
address = ""
max = 0

for line in fhandle :
    line = line.rstrip()
    # Second condintion checks how much words are in the line.
    # The line we are looking for has a specific format that must consiste of 7 words
    if "From" in line and len(line.split()) == 7:
        words = line.split()
        email[words[1]] = email.get(words[1], 0) + 1
        for mail in email :
            if max < email[mail] :
                address = mail
                max = email[mail]

print(address, max)