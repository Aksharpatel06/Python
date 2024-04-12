num=[]
temp=0

for i in range(5) :
    i=int(input("enter the num:"))
    num.append(i)

for i in range(0, len(num)):    
    for j in range(i+1, len(num)):    
        if(num[i] > num[j]):    
            temp = num[i];    
            num[i] = num[j];    
            num[j] = temp;    

print()

print("Elements of array sorted in ascending order: ");    
for i in range(0, len(num)):    
    print(num[i], end=" ");    