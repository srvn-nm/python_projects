# import time
# start_time = time.time()
fullPrimeNumbers = set()
notFullPrimeNumbers = set()
def fullPrime(n):
    while n > 0:
        if (n == 1):
            notFullPrimeNumbers.add(n)
            return 0
        elif n in fullPrimeNumbers and not n in notFullPrimeNumbers:
            return 1
        elif not n in fullPrimeNumbers and n in notFullPrimeNumbers:
            return 0
            
        i = 2
        while i * i <= n :
            if (n % i == 0):
                notFullPrimeNumbers.add(n)
                return 0
            i += 1
        n = int(n/10)
        
    fullPrimeNumbers.add(n)
    return 1
    
    
    
n = int(input())
for num in range(((pow(10,(n - 1))*2) + 1),(pow(10,n)-1),2):
    if fullPrime(num) == 1:
            print(num)
# print("--- %s seconds ---" % (time.time() - start_time))