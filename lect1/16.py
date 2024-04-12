num=[]

for i in range(5) :
    i=int(input("enter the num:"))
    num.append(i)

max=0
for i in num:
    if(i>max):
        max=i

print('largest number :',max)
