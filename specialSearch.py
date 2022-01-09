import numpy as np
x=int(input("enter x: "))
n=int(input("enter n: "))
table=[]
entries=list(map(int,input().split()))
table=np.array(entries)
for i in range(0,n):
    for j in range(i,n):
        if ((abs(i-j))==x) or ((i+j)==(2*x)):
            print ("("+str(table[i])+" , "+str(table[j])+")\n")