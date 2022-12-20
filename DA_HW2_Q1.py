import time
start_time = time.time()
fullPrimeNumbers, notFullPrimeNumbers = set(), set()
def fullPrime(n):
    if (n in fullPrimeNumbers and not n in notFullPrimeNumbers) or (n == 1 or n % 2 == 0 or n % 3 == 0):
        return 0
    elif (not n in fullPrimeNumbers and n in notFullPrimeNumbers) or (n == 2 or n == 3):
        return 1
    else:
        while n > 0:
            i = 5
            w = 2
            while i * i <= n :
                if (n % i == 0):
                    notFullPrimeNumbers.add(n)
                    return 0
                i += w
                w = 6 - w
            n = int(n/10)
        
    fullPrimeNumbers.add(n)
    return 1


def printFullPrime(n):
    num = pow(10,(n - 1))
    while num <= (pow(10,n)-1):
        if fullPrime(num) == 1:
             print(num)
        num += 1
    
    
    
    
printFullPrime(int(input()))
print("--- %s seconds ---" % (time.time() - start_time))