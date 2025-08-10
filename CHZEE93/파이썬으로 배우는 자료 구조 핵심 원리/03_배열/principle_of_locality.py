# 시간 지역성 : 한번 접근한 변수는 다시 접근할 가능성이 높음
# 공간 지역성 : 접근한 변수는 이전의 접근한 변수 근처에 있을 가능성이 높음
# CPU(Register) <-> Cache


def sum_arr(arr):
    ret = 0
    for elem in arr:
        ret += elem
    return ret
