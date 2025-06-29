#백준 2003번(수들의 합2)

import sys

N, M = map(int, sys.stdin.readline().split())
aList = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
total = 0
cnt = 0

while True:
    if total >= M:
        total -= aList[start]
        start += 1
    elif end == N:
        break
    else:
        total += aList[end]
        end += 1

    if total == M:
        cnt += 1

print(cnt)
