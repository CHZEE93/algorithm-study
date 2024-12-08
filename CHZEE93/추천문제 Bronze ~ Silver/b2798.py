#백준 2798번
N, M = map(int, input().split())
nList = list(map(int, input().split()))

maxNum = 0

for i in range(N):
    sNum = 0
    for j in range(i+1,N):
        for k in range(j+1,N):
            sNum = nList[i] + nList[j] + nList[k]
            maxNum = sNum if sNum > maxNum and sNum <= M else maxNum

print(maxNum)
