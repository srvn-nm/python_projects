def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)
  
    # range(for buckets)
    rnge = (max_ele - min_ele) / noOfBuckets
  
    temp = []
  
    # create empty buckets
    for i in range(noOfBuckets):
        temp.append([])
  
    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)
  
        # append the boundary elements to the lower array
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
  
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
  
    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
                for i in range(1, len(temp)):
                    up = temp[i]
                    j = i - 1
                    while j >= 0 and temp[j] > up: 
                        temp[j + 1] = temp[j]
                        j -= 1
                    temp[j + 1] = up     
  
    # Gather sorted elements 
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1
  
  
# Driver Code
arr = [ 3, 2, 3, 1 ]
bucketSort(arr, int(len(arr)/2))
print(arr)