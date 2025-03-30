#백준 1874번(스택 수열)

import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []
current = 1

for target in sequence:
    while current <= target:
        stack.append(current)
        result.append("+")
        current += 1
    
    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break
else:
    print("\n".join(result))
