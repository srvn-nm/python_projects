def fibo(num) :
    if num == 0 :
        return 0
    elif num == 1 :
        return 1
    elif num > 1 :
        return fibo(num - 1) + fibo(num - 2)
    else :
        print('Sorry. You entered an invalid number.')
number = int(input('please enter the end of your range here : '))
x = 0
while x <= number :
    print(f'the {x}th number is ' + str(fibo(x)))
    x+=1