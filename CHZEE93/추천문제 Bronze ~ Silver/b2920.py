#백준 2920번
jList = list(map(int,input().split()))

res = ''

for i in range(len(jList)):
    if i == 0 :
        continue
    elif i>0 and jList[i-1] - 1 == jList[i]:
        res = 'descending'
    elif i>0 and jList[i-1] + 1 == jList[i]:
        res = 'ascending'
    else:
        res = 'mixed'
        break
        
print(res)
