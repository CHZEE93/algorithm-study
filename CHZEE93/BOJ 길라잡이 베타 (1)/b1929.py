#백준 1929번(소수구하기)

import sys
input = sys.stdin.read

m, n = map(int, input().split())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

for i in range(m, n+1):
    if is_prime[i]:
        print(i)
