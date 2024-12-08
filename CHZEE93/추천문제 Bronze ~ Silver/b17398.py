#백준 17389번

N = int(input())
lox = list(input())

score = 0
bScore = 0

for i in range(N):
    if lox[i] == 'O':
        score += (i+1)
        score += bScore
        bScore += 1
    else:
        bScore = 0

print(score)
