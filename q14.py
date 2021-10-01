num = int(input('Please type your number to be checked here : '))
result = 0
for i in range(1,num): 
    if num % i == 0 :
        result += i
if result == num :
    print('The given number was pefect.')
else: print('The given number was not pefect.')