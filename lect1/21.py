def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

def module(num1, num2):
    if num2 != 0:
        return num1 % num2
    else:
        return "Cannot modulo by zero"

def default(num1, num2):
    return "Incorrect operation"

switcher = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division,
    5: module
}

print('''You can perform operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Module ''')

choice = int(input("Select operation from 1 to 5: "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = switch(choice, num1, num2)
print("Result:", result)
