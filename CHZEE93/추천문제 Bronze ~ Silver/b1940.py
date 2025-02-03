#백준 1940번
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
nList = list(map(int,sys.stdin.readline().split()))

nList.sort()

left = 0
right = N -1
cnt = 0

while left < right:
    current_sum = nList[left] + nList[right]
    if current_sum == M:
        cnt += 1
        left += 1
        right -= 1
    elif current_sum < M:
        left += 1
    else:
        right -= 1

print(cnt)

    
