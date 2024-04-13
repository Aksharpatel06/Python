def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)

num = int(input('Enter the number: '))

print('the sum of digits of a number:', sum(num))
