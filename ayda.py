inputString = input().upper()
s=[]
for i in inputString:
    if not i.isalpha():
        inputString=inputString.replace(i,' ')
for i in inputString.split():
    s.append(i)
s.reverse()
for i in s:
    print(i,end="\n")