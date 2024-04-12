num=[]

for i in range(5) :
    i=int(input("enter the num:"))
    num.append(i)

sum=0
for i in num:
    sum+=i

print('sum of all element:',sum)
