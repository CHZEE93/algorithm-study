#백준 10808번

sList = list(input())

aList = [0] * 26

for i in range(len(sList)):
    tmp = aList[(int(ord(sList[i])) - 97)]
    aList[(int(ord(sList[i])) - 97)] = int(tmp) + 1

for i in range(len(aList)):
    print(aList[i], end=' ')
