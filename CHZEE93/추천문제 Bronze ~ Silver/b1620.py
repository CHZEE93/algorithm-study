# 백준 1620번

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())

name_to_num = {}
num_to_name = {}

for i in range(1, N + 1):
    name = data[i]
    name_to_num[name] = i
    num_to_name[i] = name

result = []
for q in data[N + 1:]:
    if q.isdigit():  # 숫자인 경우
        result.append(num_to_name[int(q)])
    else:  # 이름인 경우
        result.append(name_to_num[q])

sys.stdout.write("\n".join(map(str, result)) + "\n")
