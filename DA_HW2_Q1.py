# import time
# start_time = time.time()
fullPrimeNumbers = set()
notFullPrimeNumbers = set()
def fullPrime(n):
    if n in fullPrimeNumbers and not n in notFullPrimeNumbers:
        return 1
    elif not n in fullPrimeNumbers and n in notFullPrimeNumbers:
        return 0
    else:
        while n > 0:
            if (n == 1):
                notFullPrimeNumbers.add(n)
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
num = pow(10,(n - 1))
while num <= (pow(10,n)-1):
    if fullPrime(num) == 1:
            print(num)
    num += 1
# print("--- %s seconds ---" % (time.time() - start_time))