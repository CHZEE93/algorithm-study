#백준 1748번

N = int(input())
result = 0
length = 1
start = 1

while start <= N:
    end = start * 10 - 1
    if end > N:
        end = N
    result += (end - start + 1) * length
    length += 1
    start *= 10

print(result)
