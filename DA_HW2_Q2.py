def merge(arr, temp, l, m, r) :
 
    # i: index to left subarray
    i = l
  
    # j: index to right subarray
    j = m + 1
  
    # Stores count of pairs that
    # satisfy the given condition
    cnt = 0
    for l in range(m + 1) :
        found = False
  
        # Traverse to check for the
        # valid conditions
        while (j <= r) :
  
            # If condition satisfies
            if (arr[i] > arr[j]) :
                found = True        
            else :
                break
            j += 1
  
        # While a[i] > K*a[j] satisfies
        # increase j
  
        # All elements in the right
        # side of the left subarray
        # also satisfies
        if (found) :
            cnt += j - (m + 1)
            j -= 1
  
    # Sort the two given arrays and
    # store in the resultant array
    k = l
    i = l
    j = m + 1
  
    while (i <= m and j <= r) :
        if (arr[i] <= arr[j]) :
            temp[k] = arr[i]
            k += 1
            i += 1
        else :
            temp[k] = arr[j]
            k += 1
            j += 1
  
    # Elements which are left
    # in the left subarray
    while (i <= m) :
        temp[k] = arr[i]
        k += 1
        i += 1
  
    # Elements which are left
    # in the right subarray
    while (j <= r) :
        temp[k] = arr[j]
        k += 1
        j += 1
    for i in range(l, r + 1) :
        arr[i] = temp[i]
  
    # Return the count obtained
    return cnt
  
# Function to partition array into two halves
def mergeSortUtil(arr, temp, l, r) :
    cnt = 0
    if (l < r) :
  
        # Same as (l + r) / 2, but avoids
        # overflow for large l and h
        m = (l + r) // 2
  
        # Sort first and second halves
        cnt += mergeSortUtil(arr, temp, l, m)
        cnt += mergeSortUtil(arr, temp, m + 1, r)
  
        # Call the merging function
        cnt += merge(arr, temp, l, m, r)
    return cnt
  
# Function to print the count of
# required pairs using Merge Sort
def mergeSort(arr, N) :
    temp = [0]*N
    print(mergeSortUtil(arr, temp, 0, N - 1))
 
  # Driver code
arr = [ 5, 6, 2, 5 ]
N = len(arr)
 
# Function Call
mergeSort(arr, N, K)