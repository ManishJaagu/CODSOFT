''' Author- Jagu Manish || Python Programming Internship at CodSoft

------------------TASK 2 -CALCULATOR-----------------------
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.

IDE used: VS Code
'''


print("\n")
print("                              ╔═══════════════════════════════════════════════════════╗")
print("                              ║                   C A L C U L A T O R                 ║")
print("                              ╚═══════════════════════════════════════════════════════╝")
print("\n")

#Importing modules
import os  

# functions for different mathematical operations
def addition(a, b):
    return a + b

def subtraction( a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a,b):
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


operations={
    '+' : addition,
    '-' : subtraction,
    '*' : multiplication,
    '/' : division,
    '%' : modulus,
    '**': power
}

def calculator():
    num1 = int(input("Enter a number: "))  #change the datatype to float, if you want to operate decimal calculations.
    print("\nSelect an Operator:")
    for operator in operations:
        print(operator)

    continue_calculation = True
    while continue_calculation:
        input_operator = input("Enter an operator: ")
        selected_operator =operations[input_operator]

        num2 = int(input("\nEnter the next number: "))

        output = selected_operator(num1, num2)              #Here, the output variable 'output' will store the respective operator functions
        print(f"\n{num1} {input_operator} {num2} = {output}")

        continued = input(f"\nPress 'y' to continue with the output: {output}\n"
                        f"Press 'n' to start a new calculation. Press any key to exit from the calculator.    ").lower()

        if continued == 'y':
            num1 = output           #The output of previous calculation will be num1 variable now
        elif continued == 'n':
            continue_calculation = False
            os.system('cls')
            calculator()
        else:
            continue_calculation = False
            print("beep... beep... exited from the calculator!")
calculator()