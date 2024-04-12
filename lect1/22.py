def factorail(n):
    if n<=1:
        return 1
    else:
        return n*factorail(n-1)

num1 = float(input("Enter the number: "))

recursion = factorail(num1)

print('the factorial of a number :',recursion)
