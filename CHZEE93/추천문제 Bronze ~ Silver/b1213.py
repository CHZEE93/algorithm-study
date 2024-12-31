#백준 1213번

from collections import Counter

s = input().strip()

counter = Counter(s)

# 홀수 빈도를 가진 문자 확인
odd_count = 0
odd_char = ''
for char, count in counter.items():
    if count % 2 != 0:
        odd_count += 1
        odd_char = char

# 홀수 빈도가 두 개 이상이면 불가능
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    half = []
    for char, count in sorted(counter.items()):
        half.append(char * (count // 2))

    center = odd_char if odd_count == 1 else ''

    palindrome = ''.join(half) + center + ''.join(half[::-1])
    print(palindrome)
