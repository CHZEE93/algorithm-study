#백준 3474번 

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    number = int(sys.stdin.readline())
    count = 0
    divisor = 5

    while number >= divisor:
        count += number // divisor
        divisor *= 5

    print(count)
