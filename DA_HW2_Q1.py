def fullPrime(n):
    if (n == 1):
        return 0
         
    i = 2
    while i * i <= n and n > 1 :
        if (n % i == 0):
            return 0
        i += 1
        n %= 10
    return 1