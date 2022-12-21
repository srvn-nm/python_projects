import time
start_time = time.time()
import functools
fullPrimeNumbers, notFullPrimeNumbers = set(), set()
@functools.lru_cache(maxsize=300)

def fullPrime(n):
    i = 5
    w = 2
    while n > 0:
        if (n in fullPrimeNumbers and not n in notFullPrimeNumbers) or (n == 1 or n % 2 == 0 or n % 3 == 0 or n < 0):
            return 0
        elif (not n in fullPrimeNumbers and n in notFullPrimeNumbers) or (n == 2 or n == 3):
            return 1
        while i * i <= n :
            if (n % i == 0):
                notFullPrimeNumbers.add(n)
                return 0
            i += w
            w = 6 - w
        n = (int(n/10))
        
    fullPrimeNumbers.add(n)
    return 1
    
    
    
n = int(input())
for num in range(pow(10,(n - 1)),(pow(10,n))):
        if fullPrime(num) == 1:
             print(num)
print("--- %s seconds ---" % (time.time() - start_time))