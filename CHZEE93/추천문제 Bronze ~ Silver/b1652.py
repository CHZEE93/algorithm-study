#백준 1652번
def count_bed_positions(N, room):
    horizontal_count = 0
    vertical_count = 0

    # 가로 방향 탐색
    for row in room:
        count = 0
        for cell in row:
            if cell == '.':
                count += 1
            else:
                if count >= 2:
                    horizontal_count += 1
                count = 0
        if count >= 2:
            horizontal_count += 1

    # 세로 방향 탐색
    for col in range(N):
        count = 0
        for row in range(N):
            if room[row][col] == '.':
                count += 1
            else:
                if count >= 2:
                    vertical_count += 1
                count = 0
        if count >= 2:
            vertical_count += 1

    return horizontal_count, vertical_count

# 입력 받기
N = int(input())
room = [input().strip() for _ in range(N)]

# 결과 출력
horizontal, vertical = count_bed_positions(N, room)
print(horizontal, vertical)
