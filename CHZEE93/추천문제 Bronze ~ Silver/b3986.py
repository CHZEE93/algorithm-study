#백준 3986번

N = int(input())

cnt = 0

for _ in range(N):
    text = input()
    stack = []
    
    for char in text:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if not stack:
        cnt += 1

print(cnt)
