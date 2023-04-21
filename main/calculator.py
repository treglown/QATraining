number = int(input("Select a number!"))

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def squared(x, y):
    return x * x

while True:
    answer = input("What would you like to do? A. Addition, B. Subtract, C. Divide, D. Multiply, E. Square?")

    if answer in ('A', 'B', 'C', 'D', 'E'):
        try:
            number1 = float(input("Number1:"))
            number2 = float(input("NUmber2:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        if answer == 'A':
            print(number1, "+", number2, "=", addition(number1, number2))

        elif answer == 'B':
            print(number1, "-", number2, "=", subtract(number1, number2))
        
        elif answer == 'C': 
            print(number1, "/", number2, "=", divide(number1, number2))
        
        elif answer == 'D':
            print(number1, "*", number2, "=", multiply(number1,  number2))

        elif answer == 'E':
            print(number1, "*",  number1, "=", squared(number1, number1))

    else:
        print("That is an invalid input")