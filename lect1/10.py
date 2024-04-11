prime_num = int(input("Enter a number: "))

flag = False

if prime_num == 1:
    print(prime_num, "is not a prime number")
elif prime_num > 1:
    for i in range(2, prime_num):
        if (prime_num % i) == 0:
            flag = True
            break
    if flag:
        print(prime_num, "is not a prime number")
    else:
        print(prime_num, "is a prime number")