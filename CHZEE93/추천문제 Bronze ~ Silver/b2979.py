#백준 2979번

A, B, C = map(int, input().split())

tList = [0] * 100

for i in range(3):
    S, E = map(int,input().split())
    
    for j in range(S,E):
        tList[j] += 1

result = 0       

for i in range(len(tList)):
    if(tList[i] == 1):
        result += A
    elif(tList[i] == 2):
        result += B*2
    elif(tList[i] == 3):
        result += C*3

print(result)
