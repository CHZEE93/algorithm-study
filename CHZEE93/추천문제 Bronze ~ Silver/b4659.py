#백준 4659번

vowels  = ['a','e','i','o','u']

while True:
    S = input()
    result = "acceptable."
    if S == "end":
        break

    #모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    contains_vowel = any(char in vowels for char in S)

    if not contains_vowel:
        result = "not acceptable."

    for i in range(len(S)):
        #같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다
        if (S[i] != 'e' and S[i] != 'o' and ((i+1) < len(S)) and  S[i] == S[i+1]):
            result = "not acceptable."

        if(((i+2)<len(S)) and (((S[i] in vowels) and (S[i+1] in vowels) and (S[i+2] in vowels)) or ((S[i] not in vowels) and (S[i+1] not in vowels) and (S[i+2] not in vowels)))):
            result = "not acceptable."

    

    print("<%s> is %s" %(S, result) )
