base=int(input('enter the base:'))
num=int(input('enter the exponent:'))
result=1
while num!=0:
    result*=base
    num-=1

print('answer:',str(result))