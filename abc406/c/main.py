n = int(input())
p = list(map(int, input().split()))

if n < 4:
    print(0)
    exit()

d = [p[i + 1] > p[i] for i in range(n - 1)]

runs = []
counts = []
cur = d[0]
c = 1
for x in d[1:]:
    if x == cur:
        c += 1
    else:
        runs.append(cur)
        counts.append(c)
        cur = x
        c = 1
runs.append(cur)
counts.append(c)

ans = 0
for i in range(1, len(runs) - 1):
    if not runs[i] and runs[i - 1] and runs[i + 1]:
        ans += counts[i - 1] * counts[i + 1]
print(ans)
