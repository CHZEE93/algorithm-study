#백준 1110번

N = int(input())
strN = '-1'

num1 = 0 if N < 10 else N//10
num2 = N%10
    
cnt = 0
    
while N != int(strN):
    tmp = num1
    num1 = num2
    num2 = (tmp+num2) % 10
    
    strN = str(num1) + str(num2)
    cnt = cnt + 1

print(cnt)
