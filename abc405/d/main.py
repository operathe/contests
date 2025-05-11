from collections import deque

h, w = map(int, input().split())
s = [list(input().rstrip()) for _ in range(h)]
p = [[-1] * w for _ in range(h)]
dq = deque()
for i in range(h):
    for j in range(w):
        if s[i][j] == "E":
            p[i][j] = 0
            dq.append((i, j))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while dq:
    x, y = dq.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#" and p[nx][ny] == -1:
            p[nx][ny] = p[x][y] + 1
            dq.append((nx, ny))

ans = [[""] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            ans[i][j] = "#"
        elif s[i][j] == "E":
            ans[i][j] = "E"
        else:
            d = p[i][j]
            for dx, dy, ch in [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < h and 0 <= nj < w and p[ni][nj] == d - 1:
                    ans[i][j] = ch
                    break

for row in ans:
    print("".join(row))
