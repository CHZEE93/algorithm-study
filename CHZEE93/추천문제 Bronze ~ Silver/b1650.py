#백준 11650번
N = int(input())

xy_list = [input().split() for _ in range(N)]

xy_list = [(int(x), int(y)) for x, y in xy_list]

xy_list.sort(key = lambda x : (x[0], x[1]))

for x, y in xy_list:
    print(x, y)
