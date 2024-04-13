def root(n):
    if(n==1 or n==0):
        return n
    i=1
    roots=1
    while(roots<=n):
        i+=1
        roots =i*i
    return i-1

num = int(input('Enter the number: '))

print('the square root of a number:', root(num))
