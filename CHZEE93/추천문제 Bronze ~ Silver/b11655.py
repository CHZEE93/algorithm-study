#백준 11655번
S = input()
s_list = []

for i in range(len(S)):
    if(S[i].isalpha()):
        if(ord(S[i]) > 96):
            s_list.append(chr(ord(S[i])-13) if ord(S[i])+13 > 122 else chr(ord(S[i])+13))
        else:
            s_list.append(chr(ord(S[i])-13) if ord(S[i])+13 > 90 else chr(ord(S[i])+13))
    else:
        s_list.append(S[i])

print(''.join(s_list))
