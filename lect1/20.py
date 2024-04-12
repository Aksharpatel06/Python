def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
num1=[]

for i in range(5) :
    i=int(input("enter the num:"))
    num1.append(i)
print(Remove(num1))