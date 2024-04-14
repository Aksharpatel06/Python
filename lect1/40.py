def list_index(lst, index):
    try:
        element = lst[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Index {index} is out of range for the list.")
    except Exception as e:
        print(f"An error occurred: {e}")


n = int(input('enter the size of list:'))
l1 = []*n
for i in range(n):
    num = int(input('enter the element:'))
    l1.append(num)

index= int(input('enter the correct total index of list:'))

list_index(l1,index)