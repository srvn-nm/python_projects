def fibo(num) :
    if num == 0 :
        return 0
    elif num == 1 :
        return 1
    elif num > 1 :
        return fibo(num - 1) + fibo(num - 2)
    else :
        print('Sorry. You entered an invalid number. >-<')
number = int(input('please enter the end of your range here and then you can see the next sentence if it is one of the fibonaccis : '))
x = 0
print('\n')
while x <= number :
    print(f'the {x}th number is ' + str(fibo(x)))
    x+=1
y = 0 
while fibo(y) != number and fibo(y) < number + 1: 
    y += 1 
if fibo(y) == number and fibo(y) < number + 1 :
    print(f'\nthe fibonacci sentence after the number you entered is : {fibo(y+1)} ^-^ \n')
else : 
    print('\nit was not one of fibonacci sentences. >-<')