#백준 10814번
N = int(input())
members = [input().split() for _ in range(N)]

members = [(int(age), name) for age, name in members]

members.sort(key= lambda x: x[0] )

for age, name in members:
    print(age, name)
