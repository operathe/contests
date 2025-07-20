h, w, n = map(int, input().split())

xy = [list(map(int, input().split())) for _ in range(n)]

q = int(input())

queries = [list(map(int, input().split())) for _ in range(q)]

row_adj = [[] for _ in range(h + 1)]
col_adj = [[] for _ in range(w + 1)]
row_count = [0] * (h + 1)
col_count = [0] * (w + 1)

for x, y in xy:
    row_adj[x].append(y)
    col_adj[y].append(x)
    row_count[x] += 1
    col_count[y] += 1

row_removed = [False] * (h + 1)
col_removed = [False] * (w + 1)

ans_list = []
for t, s in queries:
    if t == 1:
        ans_list.append(str(row_count[s]))
        if not row_removed[s]:
            row_removed[s] = True
            for y in row_adj[s]:
                if not col_removed[y]:
                    col_count[y] -= 1
            row_count[s] = 0
    else:
        ans_list.append(str(col_count[s]))
        if not col_removed[s]:
            col_removed[s] = True
            for x in col_adj[s]:
                if not row_removed[x]:
                    row_count[x] -= 1
            col_count[s] = 0


for ans in ans_list:
    print(ans)
