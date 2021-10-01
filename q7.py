import math
num = int(input('Please enter the end of the range here : '))
for i in range(2,num+1): 
    if(i == 2 or i == 3):
            print(i)
    for j in range(2,int(math.sqrt(i)+1)) :
        if(i % j == 0 and i != j): 
            break
        elif(i % j != 0 and j >= int(math.sqrt(i))):
            print(i)