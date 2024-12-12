#백준 2816번

N = int(input())

ch_list = [input() for _ in range(N)] 
result = ['1'] * ch_list.index('KBS1')

idx1 = ch_list.index('KBS1')

for i in range(idx1, 0, -1):
    result.append('4')
    tmp = ch_list[i-1]
    ch_list[i-1] = ch_list[i]
    ch_list[i] = tmp

idx2 = ch_list.index('KBS2')

if idx2>1:
    result += ['1'] * ch_list.index('KBS2')

for i in range(idx2, 1, -1):
    result.append('4')
    tmp = ch_list[i-1]
    ch_list[i-1] = ch_list[i]
    ch_list[i] = tmp
    
print(''.join(result))
