print(
    """Pythagoras' Calculator
        Find the length of A given B and C
        Find the length of B given A and C
        Find the length of C given A and B
    """
    )
user_choice = input(
    """Please select which side you want to calculate.
        1 = Side A
        2 = Side B
        3 = Side C
    """
)

if user_choice == "1":
    sideB = float(input("Enter the length of side B:"))
    sideC = float(input("Enter the length of side C: "))
    sideA = (sideB**2 - sideC**2) ** 0.5 
    print("Length of side A is ", sideA)
elif user_choice == "2":
    sideA = float(input("Enter the length of side A:"))
    sideC = float(input("Enter the length of side C: "))
    sideB = (sideA**2 - sideC**2) ** 0.5 
    print("Length of side B is ", sideB)
elif user_choice == "3":
    sideA = float(input("Enter the length of side A:"))
    sideB = float(input("Enter the length of side B: "))
    sideC = (sideA**2 + sideB**2) ** 0.5 
    print("Length of side C is ", sideC)
else: 
    print("Incorrect choice!")


