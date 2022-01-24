n=int(input())
cities = []
for i in range(n):
    cities.append(input())
k=int(input())
jobs = []
res=[]
result = 0
for j in range(k):
    jobs.append(input())
for i in jobs:
    if (len(res)<n-1) and not(i in res):
        res.append(i)
    elif len(res)==n-1 and not(i in res):
        res.clear()
        result += 1 
    else: continue 
print (result)