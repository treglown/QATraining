mark = int(input("What is your achieved grade?"))

if mark >= 85:
    print("You have achieved Distinction")
elif 65 <= mark <= 85:
    print("You have achieved a Pass")
else: 
    if mark <= 65:
        print("You have achieved a fail")