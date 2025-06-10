#백준 1182번(부분수열의 합)

from itertools import combinations

N, S = map(int,input().split())

aList = list(map(int,input().split()))

result = 0

for i in range(N+1) :
    for comb in combinations(aList, i):
        if len(comb) > 0:
            sumNum = sum(comb)
            if sumNum == S :
                result = result + 1



print(result)
