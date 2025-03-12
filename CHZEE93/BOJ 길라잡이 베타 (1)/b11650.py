#백준 11650번(좌표 정렬하기)
N = int(input())

points = []

for _ in range(N):
    xyList = list(map(int, input().split()))
    points.append(xyList)

points.sort(key=lambda p: (p[0], p[1]))

for point in points:
    print(str(point[0]) + ' ' + str(point[1]))
    
