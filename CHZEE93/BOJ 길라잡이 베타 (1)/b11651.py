#백준 11651번(좌표 정렬하기 2)

N = int(input())

points = []

for _ in range(N):
    points.append(list(map(int, input().split())))


points.sort(key=lambda p : (p[1], p[0]))

for point in points:
    print(str(point[0]) + ' ' + str(point[1]))
