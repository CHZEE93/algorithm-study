#백준 2751번(수 정렬하기2)

import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

N = int(sys.stdin.readline())
nArr = []

for _ in range(N):
    nArr.append(int(sys.stdin.readline()))

nArr = merge_sort(nArr)

print('\n'.join([str(nFactor) for nFactor in nArr]))
