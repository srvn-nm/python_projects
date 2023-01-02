# import time
# start_time = time.time()
def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    invCount = 0
    temp = [0 for x in range(right - left + 1)]
 
    while (i < mid) and (j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
 
        else:
            temp[k] = arr[j]
            invCount += mid - i
            k += 1
            j += 1
 
    while i < mid:
        temp[k] = arr[i]
        k += 1
        i += 1
 
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
 
    k = 0
    for i in range(left, right + 1):
        arr[i] = temp[k]
        k += 1
 
    return invCount
 
 
def mergeSort(arr, left, right):
    invCount = 0
 
    if right > left:
        mid = (right + left) // 2
 
        invCount = mergeSort(arr, left, mid)
        invCount += mergeSort(arr, mid + 1, right)
        invCount += merge(arr, left, mid + 1, right)
 
    return invCount
 
n = int(input())  
arr = [0]*n
for i in range(n): 
    arr[i] = int(input())
print(mergeSort(arr, 0, n - 1)%100000)
# print("--- %s seconds ---" % (time.time() - start_time))