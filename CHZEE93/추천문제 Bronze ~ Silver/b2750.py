#백준 2750번
N = int(input())
nList = []

for i in range(N):
    nList.append(int(input()))
    
for i in range(len(nList)):
    for j in range(i,len(nList)):
        if nList[i] > nList[j]:
            tmp = nList[i]
            nList[i] = nList[j]
            nList[j] = tmp
            
for i in range(len(nList)):
    print(nList[i])
