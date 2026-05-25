# CALCULATOR.

logo = '''
  
   
 _____________________
|  _________________  |
| |Welcome!         | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
   '''

# Add.
def add(n1, n2):
    return n1 + n2

# Subtract.
def subtract(n1, n2):
    return n1 - n2

# Multiply.
def multiply(n1, n2):
    return n1 * n2

# Divide.
def divide(n1, n2):
    return n1 / n2

operations = {
    
    "/": divide,
    "*": multiply,
    "+": add,
    "-": subtract
}

def calculator():
    print(logo)
    num1 = float(input("What's your first number?\n"))
    print("\n")
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Select Operations from the above list.\n")
        num2 = float(input("What's your another number?\n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}")
        if (input(f"Type 'y' for continue or Type 'n' for exit.\n")) == 'y':
            num1 = answer
        else:
            should_continue = False
            # calculator()

calculator()
        





# operation_symbol = input("Select Operations from the above list.\n")
# num3 = int(input("What's your next number?\n"))
# calculation_function = operations[operation_symbol]
# answer2 = calculation_function(calculation_function(num1, num2), num3)

# print(f"{answer1} {operation_symbol} {num3} = {answer2}")