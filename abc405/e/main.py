MOD = 998244353
A, B, C, D = map(int, input().split())

max_n = max(A + B - 1, B + C + D)

fact = [1] * (max_n + 1)
invfact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact[max_n] = pow(fact[max_n], MOD - 2, MOD)
for i in range(max_n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD


ans = 0
for i in range(B + 1):
    ways1 = comb(A + i - 1, A - 1)
    ways2 = comb((B - i) + C + D, C)
    ans = (ans + ways1 * ways2) % MOD

print(ans)
