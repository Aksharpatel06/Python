C=1
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    C = 1  
    for k in range(1,i+1):
        print(' ', C, sep='', end='')
        C = C * (i - k) // k
    print()