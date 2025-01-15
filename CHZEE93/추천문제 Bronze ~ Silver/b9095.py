# 백준 9095번 (1, 2, 3 더하기)

N = int(input()) 
list_N = [int(input()) for _ in range(N)]
max_N = max(list_N)

dp = [0] * (max_N + 1)
dp[1] = 1
if max_N >= 2:
    dp[2] = 2
if max_N >= 3:
    dp[3] = 4

for i in range(4, max_N + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for factor_N in list_N:
    print(dp[factor_N])
