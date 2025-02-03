#백준 9012번

import sys

N = int(sys.stdin.readline())

for _ in range(N):
    res = "YES"
    stack = []
    text = sys.stdin.readline()
    
    for char in text.strip():
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                res = "NO"
                break

    if len(stack) > 0 :
        res = "NO"
    
    print(res)

