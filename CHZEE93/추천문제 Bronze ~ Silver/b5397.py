#백준 5397번
import sys

for _ in range(int(sys.stdin.readline().strip())):
    commands = sys.stdin.readline().strip()
    left, right = [], []

    for cmd in commands:
        if cmd == '<':
            if left:
                right.append(left.pop())
        elif cmd == '>':
            if right:
                left.append(right.pop())
        elif cmd == '-':
            if left:
                left.pop()
        else:
            left.append(cmd)

    print(''.join(left + right[::-1]))
