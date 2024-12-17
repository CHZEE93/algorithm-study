#백준 9037번

T = int(input())

for i in range(T):
    N = int(input())
    childs = list(map(int, input().split()))
    childs_temp = [0]*N
    
    cnt = 0
    for i in range(len(childs)):
            childs[i] += childs_temp[i]
            if childs[i] % 2 == 1 :
                childs[i]+=1
    
    while len(set(childs)) > 1:
        cnt += 1
        
        for i in range(len(childs)):
            j = i+1 if i < len(childs)-1 else 0
            childs_temp[j] = (childs[i]//2)
            childs[i] -= childs[i]//2

        for i in range(len(childs)):
            childs[i] += childs_temp[i]
            if childs[i] % 2 == 1 :
                childs[i]+=1
            
            
    print(cnt)
