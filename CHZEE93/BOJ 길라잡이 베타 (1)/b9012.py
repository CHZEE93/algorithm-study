#백준 9012번(괄호)

N = int(input())

for _ in range(N):
    result = "NO"
    rStack = []
    tmpList = list(input())

    for tmpFactor in tmpList:
        if(tmpFactor == "("):
            rStack.append(0)
            result = "YES"
        else:
            if len(rStack) == 0 :
                result = "NO"
                break
            rStack.pop()

    if len(rStack) > 0 :
        result = "NO"
    
    print(result)
