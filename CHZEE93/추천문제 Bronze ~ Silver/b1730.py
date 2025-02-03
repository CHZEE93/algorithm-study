#백준 1730번
N = int(input())
pan_list = [["."] * N for _ in range(N)]

move_str = str(input())
move_list = [move_char for move_char in move_str]

row = 0
col = 0

for move_char in move_list:
    if move_char not in ("U", "D", "L", "R"):
        continue 
    
    if move_char == "U" or move_char == "D":
        if (row == 0 and move_char == "U") or (row == N-1 and move_char == "D"):
            continue
        
        if pan_list[row][col] == ".":
            pan_list[row][col] = "|"
        elif pan_list[row][col] != "|":
            pan_list[row][col] = "+"

        row += 1 if move_char == "D" else -1

        if pan_list[row][col] == ".":
            pan_list[row][col] = "|"
        elif pan_list[row][col] != "|":
            pan_list[row][col] = "+"

    elif move_char == "L" or move_char == "R":
        if (col == 0 and move_char == "L") or (col == N-1 and move_char == "R"):
            continue
        
        if pan_list[row][col] == ".":
            pan_list[row][col] = "-"
        elif pan_list[row][col] != "-":
            pan_list[row][col] = "+"

        col += 1 if move_char == "R" else -1

        if pan_list[row][col] == ".":
            pan_list[row][col] = "-"
        elif pan_list[row][col] != "-":
            pan_list[row][col] = "+"

for i in range(len(pan_list)):
    for j in range(len(pan_list[i])):
        print(pan_list[i][j], end="")
    print()
