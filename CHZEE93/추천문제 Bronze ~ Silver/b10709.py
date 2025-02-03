# 백준 10709번

H, W = map(int, input().split())

cList = []
rList = [[-1 for _ in range(W) ]  for _ in range(H)]

for i in range(H):
    S = input()
    cList.append([Schar for Schar in S])

for i in range(H):
    c_count = -1;
    for j in range(W):
        if c_count >= 0 :
            c_count += 1
        if cList[i][j] == 'c':
            c_count = 0
        rList[i][j] = c_count

for rowList in rList:
    for colValue in rowList:
        print(colValue, end=' ')
    print()
