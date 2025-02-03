#백준 8979번
N, K = map(int, input().split())
countries = []

for _ in range(N):
    country_data = list(map(int, input().split()))
    countries.append(country_data)

countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
ranks = [0] * N

for i in range(N):
    if i > 0 and countries[i][1:] == countries[i - 1][1:]:
        ranks[i] = ranks[i - 1]
    else:
        ranks[i] = rank
    rank += 1

for i in range(N):
    if countries[i][0] == K:
        print(ranks[i])
        break
