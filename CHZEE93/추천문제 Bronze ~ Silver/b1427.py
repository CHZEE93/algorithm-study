# 백준 1427번

S = input()
iList = []

for i in range(len(S)):
    iList.append(int(S[i]))
    
for i in range(len(iList)):
    for j in range(i+1, len(iList)):
        if(iList[i] < iList[j]):
            tmp = iList[i]
            iList[i] = iList[j]
            iList[j] = tmp
    
print(''.join(map(str,iList)))
