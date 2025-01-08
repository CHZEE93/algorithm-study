# 백준 1966번
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    count = 0
    while queue:
        current = queue.popleft()
        
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == m:
                print(count)
                break
