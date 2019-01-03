import re

fname = input("Enter File Name: ")
fhandle = open(fname)

file_num_sum = 0

for line in fhandle :
    if re.search('[0-9]+', line) :
        string_num = re.findall('[0-9]+', line)
        for str_num in string_num :
            num = int(str_num)
            file_num_sum = file_num_sum + num

print(file_num_sum)