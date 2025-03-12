#백준 10845번(큐)
import sys

N = int(sys.stdin.readline())

result = []

for _ in range(N):
    comms = sys.stdin.readline().split()

    if comms[0] == "push":
        result.append(int(comms[1]))
    elif comms[0] == "pop":
        rLen = len(result)

        if rLen > 0 :
            sys.stdout.write(str(result[0])+ '\n')
            result = result[1:rLen]
        else:
            sys.stdout.write("-1"+ '\n')
    elif comms[0] == "size":
        rLen = len(result)
        sys.stdout.write(str(rLen)+ '\n')
    elif comms[0] == "empty":
        rLen = len(result)

        if rLen > 0 :
            sys.stdout.write("0"+ '\n')
        else:
            sys.stdout.write("1"+ '\n')
    elif comms[0] == "front":
        rLen = len(result)

        if rLen > 0 :
            sys.stdout.write(str(result[0])+ '\n')
        else:
            sys.stdout.write("-1"+ '\n')
    elif comms[0] == "back":
        rLen = len(result)

        if rLen > 0 :
            sys.stdout.write(str(result[rLen-1])+ '\n')
        else:
            sys.stdout.write("-1"+ '\n')
