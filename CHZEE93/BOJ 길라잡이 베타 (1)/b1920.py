#백준 1920번 (수 찾기)
import sys

#set로 변경!!
N = int(sys.stdin.readline())
nList = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))

for num in mList:
    if num in nList:
        print(1)
    else:
        print(0)
