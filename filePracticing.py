myFile = open("./filePractice.txt", 'r')
info = myFile.readlines()
for i in range(len(info)) :
    print(info[i],end='\n^-^\n\n')