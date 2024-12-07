#백준 2747번
#피보나치 수열 Fn = Fn-1 + Fn-2 (n>=2)

N = int(input())

res_list =[]

for i in range(N+1):
    if i<2:
        res_list.append(i)
    else:
        res_list.append(res_list[i-1] + res_list[i-2])

print(res_list[N])
