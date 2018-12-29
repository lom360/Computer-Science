text = "X-DSPAM-Confidence:    0.8475"

# When accessing index. We can also use methods of the same string/array to access the index.
# Line 5 is an example. 1 was added to avoid including the colon.
string_num = text[(text.find(':') + 1) : ]

float_num = float(string_num)
print(float_num)