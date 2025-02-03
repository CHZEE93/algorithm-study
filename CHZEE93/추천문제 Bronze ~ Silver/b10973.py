#백준 10973번 (이전 순열)

N = int(input())
arr = list(map(int, input().split()))

len_arr = len(arr)

i = len_arr - 1

while i > 0 and arr[i-1] <= arr[i]:
    i -= 1
if i == 0:
    print(-1)
else:
    j = len_arr - 1
    while arr[j] >= arr[i-1]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    arr[i:] = reversed(arr[i:])
    print(*arr)
