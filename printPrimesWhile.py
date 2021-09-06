import math
num = int(input('Please enter the number you want to check the range up to: '))
x = 3
i = 2
print('2 is one of our prime numbers ^-^')
while x <= num :
    isPrime = True
    while i <= int(math.sqrt(x))+1 :
        if x % i == 0 and x != i :
            isPrime = False
            break
        i += 1
    if isPrime :
        print(f'{x} is one of our prime numbers ^-^')
    x += 2