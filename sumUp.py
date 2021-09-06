def sumUp(x):
    s = 0
    for i in range(1 , x + 1) : 
        s += i  
    return s
print('The resault of the sumUp function is :' + str(sumUp(int(input('enter the number : ')))))