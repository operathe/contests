# 8行の入力を受け取る
grid = []
for _ in range(8):
    row = input()
    grid.append(row)

# 駒が置かれているマスの行と列を記録する
occupied_rows = set()
occupied_cols = set()

for i in range(8):
    for j in range(8):
        if grid[i][j] == "#":
            occupied_rows.add(i)
            occupied_cols.add(j)

# 安全なマスをカウント
safe_count = 0
for i in range(8):
    for j in range(8):
        # 現在のマスが空いていて、その行と列に他の駒がないかを確認
        if grid[i][j] == "." and i not in occupied_rows and j not in occupied_cols:
            safe_count += 1

# 結果を出力
print(safe_count)
