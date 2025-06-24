#백준 9663번(N-Queen)

def n_queens(n):
    def dfs(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in columns or (row + col) in diag1 or (row - col) in diag2:
                continue
            columns.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            dfs(row + 1)
            columns.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    count = 0
    columns = set()
    diag1 = set()  # ↙ 방향 대각선
    diag2 = set()  # ↘ 방향 대각선
    dfs(0)
    return count

# 입력 및 출력
n = int(input())
print(n_queens(n))
