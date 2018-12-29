fname = input("Enter file name: ")
# If user inputs an invalid file or not the target file.
# The below statement will fix to avoid issues.
if fname != "mbox-short.txt" : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh :
    # The second part of the condition checks how much words are in the line.
    # The line format we are dealing with must only have 7 words.
    if "From" in line and len(line.split()) == 7:
        words = line.split()
        email = words[1]
        print(email)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")