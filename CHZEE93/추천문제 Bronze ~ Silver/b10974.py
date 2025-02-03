#백준 10974(모든순열)

from itertools import permutations

N = int(input())
arr = [i+1 for i in range(N)]
perms = list(permutations(arr))

for perm in perms:
    print(*perm)
