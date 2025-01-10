# 백준 17413번

text = input()
res = []
res_temp = []

isTag = False
index = 0

for char in text:
    if char == "<":
        isTag = True

    if isTag or char ==" ":
        if len(res_temp) > 0 :
            res_temp.reverse()
            for char_temp in res_temp:
                res.append(char_temp)
            
        res.append(char)
        res_temp = []
    else:
        res_temp.append(char)

    
    if char == ">":
        isTag = False

    index += 1
    
if len(res_temp) > 0 :
    res_temp.reverse()
    for char_temp in res_temp:
        res.append(char_temp)
        
res_temp = []

print("".join(res))
