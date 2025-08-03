def add_two(a,b):
    c = a + b #지역
    return c #스택프레임 소멸

#전역
a = 10
b = 20
result = add_two(a,b) #스택프레임 생성
print(result)