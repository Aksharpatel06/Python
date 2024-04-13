def average(n,n2):
    sum=0
    for i in n:
        sum+=i

    return sum/n2



num=int(input('size of array:'))
list =[]*num

for i in range(num):
    n=int(input('enter the number:'))
    list.append(n)

print('the average of elements:',average(list,num))
