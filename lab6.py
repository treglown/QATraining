personal_allowance = 11850

def tax_calculator(pay, percentage):
    return (pay * percentage) / 100

def getIncomeTax(income: float)->float:
    if income <= personal_allowance:
        return 0 
    elif  income <= 34500:
        return tax_calculator (income, 20) 
    elif income > 34500 and income < 150000:
        return tax_calculator(income, 40) 
    elif income > 150000:
        return tax_calculator(income, 45) 
    else:
        print("You must input your annual income!")

income = float(input("Input your annual income: £")) - personal_allowance
calculated_tax = getIncomeTax(income) 
print(f"Your annual tax is £{calculated_tax}")  


