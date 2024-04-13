def divine(x,y):
    try:
        result=x/y
        print('Result:',result)

    except ZeroDivisionError:
        print('The division by zero operation is not allowed.')


num1=int(input('enter the value of num1:'))
num2=int(input('enter the value of num2:'))

divine(num1,num2)