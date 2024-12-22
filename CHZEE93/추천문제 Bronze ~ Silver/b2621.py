#백준 2621번
from collections import Counter

cards = [input().split() for _ in range(5)]
colors = [card[0] for card in cards]
numbers = [int(card[1]) for card in cards]

counts = Counter(numbers) #요소별로 빈도수 Dict 형태로 출력
sorted_numbers = sorted(numbers)
most_common = counts.most_common() #(요소, 빈도수)형태로 빈도수 내림차순으로 정렬 list

score = 0

if len(set(colors)) == 1 and all(sorted_numbers[i] + 1 == sorted_numbers[i + 1] for i in range(4)):
    score = 900 + max(numbers)
elif most_common[0][1] == 4:
    score = 800 + most_common[0][0]
elif most_common[0][1] == 3 and most_common[1][1] == 2:
    score = 700 + most_common[0][0] * 10 + most_common[1][0]
elif len(set(colors)) == 1:
    score = 600 + max(numbers)
elif all(sorted_numbers[i] + 1 == sorted_numbers[i + 1] for i in range(4)):
    score = 500 + max(numbers)
elif most_common[0][1] == 3:
    score = 400 + most_common[0][0]
elif most_common[0][1] == 2 and most_common[1][1] == 2:
    score = 300 + most_common[0][0] * 10 + most_common[1][0]
elif most_common[0][1] == 2:
    score = 200 + most_common[0][0]
else:
    score = 100 + max(numbers)

print(score)
