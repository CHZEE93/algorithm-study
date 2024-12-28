#백준 1920번

import sys

N = int(sys.stdin.readline())

set_N = set(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())

list_M = list(map(int, sys.stdin.readline().split()))

for factor_M in list_M:
    if factor_M in set_N:
        print(1)
    else:
        print(0)
