a = int(input("Enter a value of first number: "))
b = int(input("Enter a value of last number: "))
flag = False

for i in range(a, b):
    if i < 2:
        continue

    for j in range(2, int(i/2)+1):
        if i % j == 0:
            flag = True
            break
    if not flag:
        print(i,'',end='')
    flag = False
