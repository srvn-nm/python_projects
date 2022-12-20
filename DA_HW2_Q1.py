# import time
# start_time = time.time()
fullPrimeNumbers = []
notFullPrimeNumbers = []
def fullPrime(n):
    if fullPrimeNumbers.count(n) == 0 and notFullPrimeNumbers.count(n) != 0:
        notFullPrimeNumbers.append(n)
        return 0
    elif fullPrimeNumbers.count(n) != 0 and notFullPrimeNumbers.count(n) == 0:
        fullPrimeNumbers.append(n)
        return 1
    elif fullPrimeNumbers.count(n) != 0 and notFullPrimeNumbers.count(n) != 0:
        while n > 0:
            if (n == 1):
                notFullPrimeNumbers.append(n)
                return 0
            
            i = 2
            while i * i <= n :
                if (n % i == 0):
                    notFullPrimeNumbers.append(n)
                    return 0
                i += 1
            n = int(n/10)
        
    fullPrimeNumbers.append(n)
    return 1


def printFullPrime(n):
    num = pow(10,(n - 1))
    while num <= (pow(10,n)-1):
        if fullPrime(num) == 1:
             print(num)
        num += 1
    
    
    
    
number = int(input())
printFullPrime(number)
# print("--- %s seconds ---" % (time.time() - start_time))