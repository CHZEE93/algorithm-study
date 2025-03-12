#백준 1181번(단어 정렬)

N = int(input())

words = [[] for _ in range(51)]

result = []

for _ in range(N):
    word = input()
    wLen = len(word)

    words[wLen].append(word)


for wList in words:
    if len(wList) > 0 :
        wList.sort()
        
        for wWord in wList:
            if not(wWord in result):
                result.append(wWord)
    
print("\n".join(result))    
