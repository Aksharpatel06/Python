def lcm(x,y):
    num=0
    if x>y:
        num=x
    else:
        num=y
    
    while(True):
        if(num%x==0 and num%y==0):
            lcms=num
            break
        num+=1

    return lcms



num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))


print("The GCD of", num1, "and", num2, "is:", lcm(num1,num2))
