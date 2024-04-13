def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac

num = int(input('Enter the number: '))

print('The factorial of the number:', factorial(num))
