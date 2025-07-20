N, Q = map(int, input().split())
A = list(map(int, input().split()))
qs = []
for i in range(Q):
    l, r, x = map(int, input().split())
    qs.append((x, l, r, i))
qs.sort()
MOD = 998244353


class FenwickSum:
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
        return self.sum(r) - self.sum(l - 1)


class FenwickMul:
    def __init__(self, n):
        self.n = n
        self.f = [1] * (n + 1)

    def mul(self, i, v):
        while i <= self.n:
            self.f[i] = self.f[i] * v % MOD
            i += i & -i

    def prod(self, i):
        s = 1
        while i > 0:
            s = s * self.f[i] % MOD
            i -= i & -i
        return s

    def range_prod(self, l, r):
        num = self.prod(r)
        den = self.prod(l - 1)
        return num * pow(den, MOD - 2, MOD) % MOD


fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD
inv = [1] * (N + 1)
inv[1] = 1
for i in range(2, N + 1):
    inv[i] = MOD - MOD // i * inv[MOD % i] % MOD

cnt_v = [0] * (N + 1)
w = [0] * (N + 1)
pos_list = [[] for _ in range(N + 1)]
for j, v in enumerate(A, start=1):
    cnt_v[v] += 1
    w[j] = cnt_v[v]
    pos_list[v].append(j)


bit_cnt = FenwickSum(N)
bit_mul = FenwickMul(N)
res = [0] * Q
cur = 1
for x, l, r, idx in qs:
    while cur < x:
        for j in pos_list[cur]:
            bit_cnt.add(j, 1)
            bit_mul.mul(j, inv[w[j]])
        cur += 1
    cnt = bit_cnt.range_sum(l, r)
    inv_denom = bit_mul.range_prod(l, r)
    res[idx] = fact[cnt] * inv_denom % MOD

print("\n".join(map(str, res)))
