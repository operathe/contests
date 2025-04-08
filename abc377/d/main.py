n, m = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# R_iの昇順でソート（同値の場合はL_iの降順）
intervals.sort(key=lambda x: (x[1], -x[0]))

total = m * (m + 1) // 2
current_max_l = 0
invalid = 0

for l, r in intervals:
    if l > current_max_l:
        delta = (l - current_max_l) * (m - r + 1)
        invalid += delta
        current_max_l = l

print(total - invalid)
