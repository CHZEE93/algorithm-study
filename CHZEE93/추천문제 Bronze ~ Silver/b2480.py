#백준 2480번

a, b, c = map(int, input().split())

if(a == b and b ==c and c==a):
    print(10000 + 1000*a)
elif(a != b and b != c and c != a):
    print(max(a,b,c) * 100)
else:
    num = a if a==b else c
    print(1000 + num*100)
    