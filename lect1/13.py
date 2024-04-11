str1 = input("Enter a first name: ")

def my_function(x):
  return x == x[::-1]

Palindrome = my_function(str1)

if Palindrome :
  print("this string is Palindrome")
else:
  print('this string is not Palindrom')
