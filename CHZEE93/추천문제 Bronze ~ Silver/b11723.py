#백준 11723번

import sys

M = int(sys.stdin.readline().strip())
S = set()

for i in range(M):
    list_input = list(sys.stdin.readline().split())
    act = ''
    num = 0

    if len(list_input) == 2:
        act = list_input[0]
        num = int(list_input[1])
    else:
        act = list_input[0]

    if act == "add" :
        S.add(num)
    elif act == "remove":
        S.discard(num)
    elif act == "check":
        print(1 if num in S else 0)
    elif act == "toggle":
        if (num in S):
            S.remove(num)
        else:
            S.add(num)
    elif act == "all":
        S =set(range(1, 21))
    elif act == "empty":
        S=set()
