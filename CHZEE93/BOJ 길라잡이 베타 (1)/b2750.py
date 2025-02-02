#백준 2750번(수 정렬하기)

import sys

N = int(sys.stdin.readline())
nList = []

for _ in range(N):
    nList.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(i,N):
        if(nList[i] > nList[j]):
            tmp = nList[i]
            nList[i] = nList[j]
            nList[j] = tmp

print(*nList)
