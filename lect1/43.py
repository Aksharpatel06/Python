alph = 65
for i in range(1,6):
    alph=65
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print(chr(alph),'',end='')
        else:
            print('  ',end='')
        alph+=1
    print()