# This is if statement practising. 

mark = int(input("What is your achieved grade?"))

if mark >= 85:
    print("You have achieved Distinction")
elif 65 <= mark <= 85:
    print("You have achieved a Pass")
else: 
    if mark <= 65:
        print("You have achieved a fail")

# This is the weight converter activity, listed below: 

weight_converter = input("What is the unit you want to convert to?")

if weight_converter == "lbs":
    kg = float(input("What is you weight in kilograms?"))
    lbs = kg * 2.204
    print("Converterd weight is", lbs)
elif weight_converter == "kg":
    lbs = float(input("What is your weight in pounds?"))
    kg = lbs / 2.204
    print("Converted weight is", kg)


counter = 0

while counter < 5:
    name = input("What is your name?")
    print(name + " is great!")
    counter += 1
    break

colours = 0

while colours == 0:
    colours = input("Name the colours of the rainbow")
    print(colours + " is a colour of the rainbow!")
    colours += 1
    if colours < 9:
        print("Great, you have named all the colours of the rainbow!")
    else:
        print("There are still a few colours that are missing")

