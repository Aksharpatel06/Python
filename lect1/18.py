

inp_str = input('enter the name:') 
 
freq = {} 
   
for ele in inp_str: 
    if ele in freq: 
        freq[ele] += 1
    else: 
        freq[ele] = 1

print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(freq))
 