n = int(input('enter the number:'))
temp = n
p = 0
 
while (n > 0):
    rem = n % 10
    p += rem ** 3
    n //= 10
    
if (temp == p):
    print("Yes. It is an Armstrong number.")
else:
    print("No. It is not an Armstrong number.")
