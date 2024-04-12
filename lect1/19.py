def intersection_list(list1, list2):  
   return set(list1).intersection(list2)  
  
num=[]

print('first list :')

for i in range(5) :
    i=int(input("enter the num:"))
    num.append(i)

print('second list :')

num1=[]

for i in range(5) :
    i=int(input("enter the num:"))
    num1.append(i)
  
print(intersection_list(num, num1))  