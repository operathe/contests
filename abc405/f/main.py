N, M = map(int, input().split())


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.f[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.f[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.sum(r) - self.sum(l - 1)


size = 2 * N
seg = []
for _ in range(M):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    seg.append((u, v))
seg.sort(key=lambda x: x[1])
Q = int(input())
qs = []
for i in range(Q):
    C, D = map(int, input().split())
    qs.append((C, D, i))
res = [0] * Q
sA = [0] * Q
sB = [0] * Q
ft = Fenwick(size)
p = 0
for C, D, idx in sorted(qs, key=lambda x: x[1]):
    while p < M and seg[p][1] < D:
        u, v = seg[p]
        ft.add(u, 1)
        p += 1
    sA[idx] = ft.sum(C - 1)
ft = Fenwick(size)
p = 0
for C, D, idx in sorted(qs, key=lambda x: x[0]):
    while p < M and seg[p][1] <= C:
        u, v = seg[p]
        ft.add(u, 1)
        p += 1
    sB[idx] = ft.sum(C - 1)
seg.sort(key=lambda x: x[0])
tA = [0] * Q
tB = [0] * Q
ft = Fenwick(size)
p = 0
for C, D, idx in sorted(qs, key=lambda x: x[1]):
    while p < M and seg[p][0] < D:
        u, v = seg[p]
        ft.add(v, 1)
        p += 1
    tA[idx] = p - ft.sum(D)
ft = Fenwick(size)
p = 0
for C, D, idx in sorted(qs, key=lambda x: x[0]):
    while p < M and seg[p][0] <= C:
        u, v = seg[p]
        ft.add(v, 1)
        p += 1
    tB[idx] = p - ft.sum(D)
for i in range(Q):
    res[i] = (sA[i] - sB[i]) + (tA[i] - tB[i])
print("\n".join(map(str, res)))
