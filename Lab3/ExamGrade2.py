level = int(input("What is your level?"))
grade = int(input("What is your mark?"))


if(level == 1):
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
if(level == 2):
    if grade <= 1:
        print("ERROR: marks must be between 1 and 100")
    elif 1 <= grade <= 40:
        print("Grade: Fail")
    elif 40 <= grade <= 50:
        print("Grade: Pass")
    elif 51 <= grade <= 65:
        print("Grade: Merit")
    elif 66 <= grade  <= 100:
        print("Grade: Distinction")
    else:
        if grade >= 100:
            print("ERROR: marks must be between 1 and 100")