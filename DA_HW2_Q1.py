def fullPrime(n):
    while n > 0:
        if (n == 1):
            return 0
         
        i = 2
        while i * i <= n :
            if (n % i == 0):
                return 0
            i += 1
        
        n = int(n/10)
    return 1


def printFullPrime(n):
    num = pow(10,(n - 1))
    while num <= (pow(10,n)-1):
        if fullPrime(num) == 1:
            print(num)
        num += 1
    
    
    
    
number = input()
printFullPrime(number)