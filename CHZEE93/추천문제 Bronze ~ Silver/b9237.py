#백준 9237번

N = int(input())
trees = list(map(int,input().split()))

trees.sort(reverse= True)

max_days = 0
for i in range(N):
    max_days = max(max_days, i + 1 + trees[i])

print(max_days + 1)
