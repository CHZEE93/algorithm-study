#백준 10867번(중복 빼고 정렬하기)

N = int(input())

result = []
nums = list(map(int,input().split()))

for i in range(N):
    if(nums[i] not in result):
        result.append(nums[i])
result.sort()

for factor in result:
    print(factor, end=' ')
