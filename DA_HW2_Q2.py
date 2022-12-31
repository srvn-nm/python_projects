from heapq import heappush, heappop
from bisect import bisect, insort
def getNumOfInversions(A):
    N = len(A)
    if N <= 1:
        return 0
    sortList = []
    result = 0
    for i, v in enumerate(A):
        heappush(sortList, (v, i))
    x = []
    while sortList:
        v, i = heappop(sortList)
        y = bisect(x, i)
        result += i - y
        insort(x, i)
    return result
 
arr = [ 3, 2, 3, 1 ]
result = getNumOfInversions(arr)%100000
print(f'Number of inversions are {result}')