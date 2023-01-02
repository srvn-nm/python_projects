def MS(arr, n):  
    temp_arr = [0]*n  
    return merge_sort(arr, temp_arr, 0, n-1)  
  
def merge_sort(arr, temp_arr, l, r):  
    ic = 0  
  
    if l < r:  
  
        mid = (l + r)//2  
  
        ic = ic +  merge_sort(arr, temp_arr, l, mid)  
  
        ic = ic + merge_sort(arr, temp_arr, mid + 1, r)  
  
        ic = ic + merge(arr, temp_arr, l, mid, r)  
    return ic  

  
def merge(arr, temp, l, m, r):  
    i = l   
    j = m + 1 
    k = l    
    ic = 0  

    while i <= m and j <= r:  
  
          
        if arr[i] <= arr[j]:  
            temp[k] = arr[i]  
            k = k + 1  
            i = i + 1  
        else:   
            temp[k] = arr[j]  
            ic = ic + (m-i + 1)  
            k = k + 1  
            j = j + 1  

    while i <= m:  
        temp[k] = arr[i]  
        k = k + 1  
        i = i + 1  

    while j <= r:  
        temp[k] = arr[j]  
        k = k + 1  
        j = j + 1  
    for n in range(l, r + 1):  
        arr[n] = temp[n]  
  
    return ic  
  
  
# Given array is  
arr = []
n = int(input())  
for index in range(n): arr[index] = int(input())
print(MS(arr, n)%100000)