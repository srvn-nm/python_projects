satr = int(input())
sutun = int(input())
table =[]
for i in range(sutun):
    table.append([int(j) for j in input().split()])
number = 3
isornot = False
for i in range(satr):
    for j in range(sutun):
        if table[i][j] == number:
            isornot = True;
            numi =i
            numj =j
if isornot:
    print("in row: "+ str(i)+" and in column: "+ str(j)+" we found number: "+ str(number))
else:
    print("Not Found")