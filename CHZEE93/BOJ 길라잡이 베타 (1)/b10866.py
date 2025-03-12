#백준 10866번(덱)

import sys

N = int(sys.stdin.readline())

nList = []

for _ in range(N):
    comms = sys.stdin.readline().split()

    if(comms[0] == "push_front"):
        nList_temp = nList
        nList = []
        nList.append(comms[1])
        nList += nList_temp
    elif(comms[0] == "push_back"):
        nList.append(comms[1])
    elif(comms[0] == "pop_front"):
        nLen = len(nList)

        if(nLen == 0):
            sys.stdout.write("-1" + "\n")
        else:
            sys.stdout.write(nList[0] + "\n")
            nList = nList[1:nLen]
    elif(comms[0] == "pop_back"):
        nLen = len(nList)

        if(nLen == 0):
            sys.stdout.write("-1" + "\n")
        else:
            sys.stdout.write(nList[nLen -1] + "\n")
            nList = nList[:nLen -1]
    elif(comms[0] == "size"):
        nLen = len(nList)
        sys.stdout.write(str(nLen) + "\n")
    elif(comms[0] == "empty"):
        nLen = len(nList)

        if(nLen == 0):
            sys.stdout.write("1" + "\n")
        else:
            sys.stdout.write("0" + "\n")
    elif(comms[0] == "front"):
        nLen = len(nList)

        if(nLen == 0):
            sys.stdout.write("-1" + "\n")
        else:
            sys.stdout.write(nList[0] + "\n")
    elif(comms[0] == "back"):
        nLen = len(nList)

        if(nLen == 0):
            sys.stdout.write("-1" + "\n")
        else:
            sys.stdout.write(nList[nLen -1] + "\n")
