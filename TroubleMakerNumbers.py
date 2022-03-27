def mergeSort(array,DangerNumber):
    
    if len(array) > 1:
        
        MiddleIndex = len(array)//2
        firstSection = array[:MiddleIndex]
        secondsection = array[MiddleIndex:]

        i = j  = 0
        while i < MiddleIndex and j < MiddleIndex:
            if firstSection[i] > 2*secondsection[j]:
                dangarous += 1
                j += 1
            elif j == MiddleIndex - 1:
                i += 1
                j = 0

        mergeSort(firstSection,DangerNumber)
        mergeSort(secondsection,DangerNumber)
         
    return DangerNumber

len_of_array = int(input())
numbers = list(map(int , input().replace(" ","")))
print(mergeSort(numbers,0))