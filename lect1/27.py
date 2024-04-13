n = int(input('enter the number:'))
p = 0
 
while (n != 0):
    rem = n % 10
    p = p*10+rem
    n //= 10


print('Reversed Number:',p)


