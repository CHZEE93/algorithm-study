#백준 1874번

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1

for target in sequence:
    while current <= target:
        stack.append(current)
        result.append("+")
        current += 1
    
    # 스택의 top이 target이면 pop
    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break
else:
    print("\n".join(result))
