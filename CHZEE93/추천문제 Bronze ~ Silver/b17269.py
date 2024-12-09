#백준 17269번
a_list = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
s_list = []

N, M = map(int, input().split())

A, B = map(list,input().split())

if N < M :
    for i in range(N):
        s_list.append(A[i])
        s_list.append(B[i])
    
    for i in range(N,M):
        s_list.append(B[i])
else :
    for i in range(M):
        s_list.append(A[i])
        s_list.append(B[i])
    
    for i in range(M,N):
        s_list.append(A[i])
        
numbers = []
for i in range(len(s_list)):
        numbers.append( a_list[ord(s_list[i]) - 65] )
    
while len(numbers) > 2 :
    new_numbers = []
    for i in range(len(numbers) - 1):
        new_numbers.append((numbers[i] + numbers[i + 1]) % 10) 
    numbers = new_numbers

result = f"{int(''.join(map(str, numbers)))}%"

print(result)
