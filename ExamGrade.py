grade = int(input("What is your grade?"))

if grade <= 1:
    print("ERROR: marks must be between 1 and 100")
elif 1 <= grade <= 50:
    print("Grade: Fail")
elif 50 <= grade <= 60:
    print("Grade: Pass")
elif 61 <= grade <= 70:
    print("Grade: Merit")
elif 71 <= grade  <= 100:
    print("Grade: Distinction")
else:
    if grade >= 100:
        print("ERROR: marks must be between 1 and 100")

