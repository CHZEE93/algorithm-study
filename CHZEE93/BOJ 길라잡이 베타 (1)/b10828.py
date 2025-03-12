#백준 10828번(스택)

import sys

N = int(sys.stdin.readline())

nList = []

for _ in range(N):
    comms = sys.stdin.readline().split()
    comm = comms[0]

    if comm == 'push':
        nList.append(int(comms[1]))
    elif comm == 'pop':
        top = len(nList) - 1
        if top < 0 :
            print(-1)
        else :
            print(nList[top])
            nList = nList[:top]
    elif comm == 'size':
        length = len(nList)
        print(length)
    elif comm == 'empty':
        top = len(nList) - 1
        if top < 0 :
            print(1)
        else :
            print(0)
    elif comm == 'top':
        top = len(nList) - 1
        if top < 0 :
            print(-1)
        else :
            print(nList[top])
