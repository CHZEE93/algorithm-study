# 백준 1406번(에디터)
import sys

text = sys.stdin.readline().strip()
N = int(sys.stdin.readline())

left = list(text)  # 커서 왼쪽에 있는 문자들
right = []         # 커서 오른쪽에 있는 문자들

for _ in range(N):
    comms = sys.stdin.readline().split()
    
    if comms[0] == "L":  # 왼쪽 이동
        if left:
            right.append(left.pop())
    
    elif comms[0] == "D":  # 오른쪽 이동
        if right:
            left.append(right.pop())
    
    elif comms[0] == "B":  # 왼쪽 문자 삭제
        if left:
            left.pop()
    
    elif comms[0] == "P":  # 새로운 문자 추가
        left.append(comms[1])

sys.stdout.write("".join(left + right[::-1]))
