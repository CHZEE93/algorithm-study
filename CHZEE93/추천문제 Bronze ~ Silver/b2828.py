#백준 2828번

N, M = map(int,input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

left = 1
right = M
move_distance = 0

for i in range(J):
    distance = 0
    
    if(apples[i] > right):
        distance = apples[i] - right
        right += distance
        left += distance
        move_distance += distance
    elif(apples[i] < left):
        distance = left - apples[i]
        right -= distance
        left -= distance
        move_distance += distance
        
print(move_distance)
