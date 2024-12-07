#백준 15969번
N = int(input())

s_list = list(map(int, input().split()))

min = 1000
max = 0

for i in range(N):
    if min >= s_list[i] :
        min = s_list[i]
    
    if max <= s_list[i] :
        max = s_list[i]
    
print(max - min)
