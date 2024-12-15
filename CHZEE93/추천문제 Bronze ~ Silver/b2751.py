#백준 2751번
import sys

n = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

numbers.sort()

for num in numbers:
    print(num)
