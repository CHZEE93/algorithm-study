#백준 17204번

N , K = map(int,input().split())

nList = [ int(input()) for _ in range(N)]

flag = 0
cnt = 0

for i in range(N):
    flag = nList[flag]
    cnt += 1
    if flag == K:
        print(cnt)
        exit(0)
print(-1)
