#백준 17427번
from sys import stdin

N = int(stdin.readline())

result = 0

for i in range(1, N + 1):
    result += i * (N // i)

print(result)
