score = input("Enter Score: ")
try :
    num_score = float(score)
except :
    num_score = -1

if num_score >= 0.9 and num_score <= 1.0 :
    print("A")
elif num_score >= 0.8 :
    print("B")
elif num_score >= 0.7 :
    print("C")
elif num_score >= 0.6 :
    print("D")
elif num_score < 0.6 and num_score >= 0:
    print("F")
else :
    print("Value of grade is out of scope!!!")