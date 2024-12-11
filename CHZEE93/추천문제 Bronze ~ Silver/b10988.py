#백준 10988번

s = str(input())

flag = 1

for i in range(len(s) // 2 ):
    if(s[i] != s[(len(s)-1) - i]):
        flag = 0
print(flag)
