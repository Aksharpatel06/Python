def reverse(n):
    return n[::-1]



num=int(input('size of array:'))
list =[]*num

for i in range(num):
    n=int(input('enter the number:'))
    list.append(n)

print('the average of elements:',reverse(list))
