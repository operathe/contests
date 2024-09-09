n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

y, z, w = 0, 0, 0
s0, s1, s2 = 0, 0, 0
ans = 0

for x in range(n):
    while y < n and s0 < p:
        s0 += a[y]
        s1 += a[y]
        y += 1
    while z < n and s1 < q:
        s1 += a[z]
        s2 += a[z]
        z += 1
    while w < n and s2 < r:
        s2 += a[w]
        w += 1
    if s0 == p and s1 == q and s2 == r:
        ans = 1
        break
    s0 -= a[x]

print("Yes" if ans else "No")
