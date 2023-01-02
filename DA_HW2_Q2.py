def MS(arr, n):  
    # A temp_arr is created to store  
    # sorted array in merge function  
    temp_arr = [0]*n  
    return merge_sort(arr, temp_arr, 0, n-1)  
  
# This Function will use MergeSort to count inversions  
  
  
def merge_sort(arr, temp_arr, l, r):  
  
    # A variable ic is used to store  
    # inversion counts in each recursive call  
  
    ic = 0  
  
      
  
  
    if l < r:  
  
          
  
        mid = (l + r)/2  
  
        # It will calculate inversion  
        # counts in the left subarray  
  
        ic = ic +  merge_sort(arr, temp_arr, l, mid)  
  
        # It will calculate inversion  
        # counts in the right subarray  
  
        ic = ic + merge_sort(arr, temp_arr, mid + 1, r)  
  
        # It will merge two subarrays in  
        # a sorted subarray  
  
        ic = ic + merge(arr, temp_arr, l, mid, r)  
    return ic  
  
# This function will merge two subarrays  
# in a single sorted subarray  
  
  
def merge(arr, temp, l, m, r):  
    i = l    # Starting index of left subarray  
    j = m + 1 # Starting index of right subarray  
    k = l    # Starting index of to be sorted subarray  
    ic = 0  
  
    # Conditions are checked to make sure that  
    # i and j don't exceed their  
    # subarray limits.  
  
    while i <= m and j <= r:  
  
          
  
        if arr[i] <= arr[j]:  
            temp[k] = arr[i]  
            k = k + 1  
            i = i + 1  
        else:  
            # Inversion will occur.  
            temp[k] = arr[j]  
            ic = ic + (m-i + 1)  
            k = k + 1  
            j = j + 1  
  
    # Copy the remaining elements of left  
    # subarray into temporary array  
    while i <= m:  
        temp[k] = arr[i]  
        k = k + 1  
        i = i + 1  
  
    # Copy the remaining elements of right  
    # subarray into temporary array  
    while j <= r:  
        temp[k] = arr[j]  
        k = k + 1  
        j = j + 1  
  
    # Copy the sorted subarray into Original array  
    for n in range(l, r + 1):  
        arr[n] = temp[n]  
  
    return ic  
  
  
# Given array is  
arr = [ 3, 2, 3, 1 ]
n = len(arr)  
result = MS(arr, n)%100000
print("The total number of inversions possible from the above array are :  ", result)
 