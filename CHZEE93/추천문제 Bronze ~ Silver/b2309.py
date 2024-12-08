#백준 2309번

iList = []
sumHeight = 0

for i in range(9):
    tmpNum = int(input())
    sumHeight += tmpNum
    iList.append(tmpNum)

resHeight = sumHeight - 100     

end = 0
for i in range(9):
    for j in range(i+1,9):
        if iList[i] + iList[j] == resHeight:
            iList.pop(j)
            iList.pop(i)
            end = 1
            break
    if end == 1:
        break
        
iList = sorted(iList)

for i in range(len(iList)):
    print(iList[i], end=' ')
