def factorial(x):
    fact = 1
    while x >= 1 :
        x , fact = x - 1 , fact * x
    return fact
print('\nThere is the resault of the factorial function : ' + str(factorial(int(input('enter your number here : ')))) + '\n')