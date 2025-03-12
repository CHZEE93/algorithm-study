#백준 1026번(보물)

N = int(input())

aList = list(map(int,input().split(' ')))
bList = list(map(int,input().split(' ')))
aList.sort(reverse=True)
bList.sort()

result = 0

for i in range(N):
    result += (aList[i] * bList[i])


print(result)
