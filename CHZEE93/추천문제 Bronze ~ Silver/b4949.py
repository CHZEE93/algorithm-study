#백준 4949번

while True:
    text = input()
    res = "yes"

    if text == ".":
        break;

    stack = []

    for char in text:
        if char == "(":
            stack.append(0)
        elif char == "[":
            stack.append(1)
        elif char == ")":
            if len(stack) == 0 or stack[len(stack)-1] == 1:
                res = "no"
                break
            stack.pop()
        elif char == "]":
            if len(stack) == 0 or stack[len(stack)-1] == 0:
                res = "no"
                break
            stack.pop()

    if res == "yes" and len(stack) == 0 :
        res = "yes"
    else:
        res = "no"
    

    print(res)
