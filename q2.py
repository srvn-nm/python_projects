n = int(input('Please type the number of the given list here : '))
list1 = []
for i in range(n) : 
    list1.append(input(f'list item {i+1} : '))
dict1 = {i:list1.count(i) for i in list1}
for i in dict1.keys():
    if dict1[i] >= n/2 : 
        print(i)