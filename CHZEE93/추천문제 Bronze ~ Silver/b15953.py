N = int(input())

prize_2017 = [500, 300, 200, 50, 30, 10]
limits_2017 = [1, 3, 6, 10, 15, 21]

prize_2018 = [512, 256, 128, 64, 32]
limits_2018 = [1, 3, 7, 15, 31]

for i in range(N):
    a, b = map(int, input().split())
    prize_a = 0
    prize_b = 0

    for j in range(6):
        if(a == 0):
            break
        if(a <= limits_2017[j]):
            prize_a = prize_2017[j]
            break

    for k in range(5):
        if(b == 0):
            break
        if(b <= limits_2018[k]):
            prize_b = prize_2018[k]
            break

    print((prize_a + prize_b) * 10000)
