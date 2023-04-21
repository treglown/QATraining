selection = int(input("What is your age?"))

if selection >= 18:
    print("You are in category A")
elif 16 <= selection <= 18:
    print("Your are in category B")
elif selection < 16:
    print("You are in category C")
