# 백준 5430번(AC)
from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr_input = input()

    if n == 0:
        nList = deque()
    else:
        nList = deque(arr_input[1:-1].split(','))

    is_reversed = False
    error_flag = False

    for cmd in p:
        if cmd == 'R':
            is_reversed = not is_reversed
        elif cmd == 'D':
            if not nList:
                print('error')
                error_flag = True
                break
            if is_reversed:
                nList.pop()
            else:
                nList.popleft()

    if not error_flag:
        if is_reversed:
            nList.reverse()
        print('[' + ','.join(nList) + ']')
