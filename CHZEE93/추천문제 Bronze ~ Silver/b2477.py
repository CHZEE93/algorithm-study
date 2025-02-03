#백준 2477번
K = int(input())
directions = []
lengths = []

for _ in range(6):
    d, l = map(int, input().split())
    directions.append(d)
    lengths.append(l)

big_width = 0
big_height = 0
for i in range(6):
    if directions[i] in (1, 2):  # 동쪽(1) or 서쪽(2)
        big_width = max(big_width, lengths[i])
    elif directions[i] in (3, 4):  # 남쪽(3) or 북쪽(4)
        big_height = max(big_height, lengths[i])

small_width = 0
small_height = 0
for i in range(6):
    if lengths[i] + lengths[(i + 1) % 6] == big_width + big_height:
        small_width = lengths[(i + 3) % 6]
        small_height = lengths[(i + 4) % 6]
        break

big_area = big_width * big_height
small_area = small_width * small_height
area = big_area - small_area

print(area * K)
