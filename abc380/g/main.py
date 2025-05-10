MOD = 998244353
inv2 = (MOD + 1) // 2
inv4 = inv2 * inv2 % MOD

N, K = map(int, input().split())
P = list(map(int, input().split()))

bit1 = [0] * (N + 1)


def add1(i, v):
    while i <= N:
        bit1[i] += v
        i += i & -i


def sum1(i):
    s = 0
    while i > 0:
        s += bit1[i]
        i -= i & -i
    return s


inv_total = 0
for x in P:
    inv_total += sum1(N) - sum1(x)
    add1(x, 1)
inv_total %= MOD

bit2 = [0] * (N + 1)


def add2(i, v):
    while i <= N:
        bit2[i] += v
        i += i & -i


def sum2(i):
    s = 0
    while i > 0:
        s += bit2[i]
        i -= i & -i
    return s


inv_w = 0
for i in range(K):
    x = P[i]
    inv_w += sum2(N) - sum2(x)
    add2(x, 1)
sum_seg = inv_w % MOD
for i in range(1, N - K + 1):
    old = P[i - 1]
    inv_w -= sum2(old - 1)
    add2(old, -1)
    new = P[i + K - 1]
    inv_w += sum2(N) - sum2(new)
    add2(new, 1)
    sum_seg = (sum_seg + inv_w) % MOD

den = N - K + 1
inv_den = pow(den, MOD - 2, MOD)
const_part = K * (K - 1) % MOD * inv4 % MOD
ans = (inv_total + const_part - sum_seg * inv_den % MOD) % MOD
print(ans)
