#백준 1037번(약수)

C = int(input())

nList = list(map(int, input().split()))

nList.sort()

result = 0

if(C % 2 == 1):
    result = nList[C//2] * nList[C//2] 
else:
    result = nList[0] * nList[C - 1]

print(result)
