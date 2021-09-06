list1 = [ 1 , 2 , 44 , 22222 , 1.81299]
list2 = [4 ,5]
def find_longest(a):
    n = 0
    for i in a :
        while n < len(str(i)) :
            n = len(str(i))
            theLongest = i
    return theLongest
print(f'\nthe longest is : {find_longest(list1)}\n')