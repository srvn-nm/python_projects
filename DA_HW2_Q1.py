# import time
# start_time = time.time()
fullPrimeNumbers, notFullPrimeNumbers = set(), set()
def fullPrime(n):
    while n > 0:
        if (not n in fullPrimeNumbers and n in notFullPrimeNumbers) or (n == 1 or (n % 2 == 0 and n != 2) or (n % 3 == 0 and n != 3)):
            notFullPrimeNumbers.add(n)
            return 0
        elif n in fullPrimeNumbers and not n in notFullPrimeNumbers or (n == 2 or n == 3):
            return 1
            
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
    
    
    
n = int(input())
for num in range(((pow(10,(n - 1))*2) + 1),(pow(10,n)-1),2):
    if fullPrime(num) == 1:
            print(num)
# print("--- %s seconds ---" % (time.time() - start_time))