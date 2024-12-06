N = int(input())
nums = list(map(int,input().split()))
result = []

for i in range(N):
    if i==0:
        result.append(nums[i])
    else:
        sum_temp = 0
        
        for j in range(len(result)):
            sum_temp += result[j]     
        
        result.append((nums[i] * (i+1)) - sum_temp)
  
for i in range(N):
    print(result[i], end=' ')
