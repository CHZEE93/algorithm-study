#백준 10815번(숫자 카드)

import sys

rArr = [0] * 20000000

N = int(sys.stdin.readline())

nList = list(map(int, sys.stdin.readline().split()))

for nNumber in nList:
    rArr[nNumber] = 1
    
M = int(sys.stdin.readline())

mList = list(map(int, sys.stdin.readline().split()))

for mNumber in mList:
    print(rArr[mNumber], end= ' ')
