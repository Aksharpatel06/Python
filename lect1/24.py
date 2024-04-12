def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Finding and printing the GCD
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)
