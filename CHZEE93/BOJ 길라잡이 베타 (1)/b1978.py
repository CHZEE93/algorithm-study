#백준 1978번(소수찾기)

def is_prime_basic(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())

nList = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if(is_prime_basic(nList[i])):
        cnt = cnt + 1

print(cnt)
