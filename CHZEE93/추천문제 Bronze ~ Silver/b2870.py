#백준 2870번

N = int(input())
nums = []

for i in range(N):
    text = input()
    new_j = 0
    for j in range(len(text)):
        
        if ord(text[j]) >= 48 and ord(text[j]) <= 57:
            if j < new_j :
                continue
            
            old_j = j
            k = j
            while k < len(text):
                if ord(text[k]) >= 48 and ord(text[k]) <= 57:
                    k = k+1
                else:
                    break
            new_j=k
            nums.append(int(text[old_j:new_j]))

nums.sort()
for num in nums:
    print(num)     
