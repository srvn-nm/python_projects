j = 0
A = [2,1,3]
B = [3,1,2]
for i in range(0,3): 
    if (A[i] != B[j]): 
        k = j
        while (A[i] != B[k]): 
            k+=1
        B[j], B[k] =B[k], B[j]
    j+=1
print(A)
print(B)