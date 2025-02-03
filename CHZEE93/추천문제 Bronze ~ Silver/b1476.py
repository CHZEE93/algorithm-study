#백준 1476번
esm_list = list(map(int, input().split()))
tmp_esm_list = [0] * 3

num = 1

while True:
    tmp_esm_list[0] = num % 15 if num % 15 != 0 else 15 
    tmp_esm_list[1] = num % 28 if num % 28 != 0 else 28
    tmp_esm_list[2] = num % 19 if num % 19 != 0 else 19
    
    if (esm_list[0] == tmp_esm_list[0] and esm_list[1] == tmp_esm_list[1] and esm_list[2] == tmp_esm_list[2]):
        break
    else:
        num += 1
    
print(num)
