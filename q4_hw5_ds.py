inputString = input().split()
nv = int(inputString[0])
nd = int(inputString[1])
def getValue(nv,nd):
    returnInt = 1
    nv2 = 0 
    if nv % 2 == 0:
        nv2 = int((nv - 2)/2)
    else:
        nv2 = int((nv + 1)/2)
    if nv2 == 0:
        nv2 = 1
    left = nv2-1
    right = nv-nv2
    if nd == 1:
        returnInt = nv + returnInt
    elif nd == nv:
        returnInt = returnInt + 1
    elif left>right:
        returnInt = returnInt + getValue(left,nd-1)
    elif left<right:
        returnInt = returnInt + getValue(right,nd)
    elif left==right:
        returnInt = returnInt + getValue(left,nd-1)
    return returnInt
    
print(int(getValue(nv,nd))-2)