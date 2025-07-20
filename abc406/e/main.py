t = int(input())
MOD = 998244353

for _ in range(t):
    n, k = map(int, input().split())
    bits = bin(n)[2:]
    L = len(bits)
    pow2 = [1] * (L + 1)
    for i in range(L):
        pow2[i + 1] = pow2[i] * 2 % MOD

    dp_count = [[0, 0] for _ in range(k + 2)]
    dp_sum = [[0, 0] for _ in range(k + 2)]
    dp_count[0][1] = 1

    for i, ch in enumerate(bits):
        b = int(ch)
        w = pow2[L - 1 - i]
        new_cnt = [[0, 0] for _ in range(k + 2)]
        new_sum = [[0, 0] for _ in range(k + 2)]
        for j in range(k + 1):
            for tight in (0, 1):
                c = dp_count[j][tight]
                if not c:
                    continue
                s = dp_sum[j][tight]
                nt = tight and b == 0
                new_cnt[j][nt] = (new_cnt[j][nt] + c) % MOD
                new_sum[j][nt] = (new_sum[j][nt] + s) % MOD
                if j + 1 <= k and (tight == 0 or b == 1):
                    nt2 = tight and b == 1
                    new_cnt[j + 1][nt2] = (new_cnt[j + 1][nt2] + c) % MOD
                    new_sum[j + 1][nt2] = (new_sum[j + 1][nt2] + s + c * w) % MOD
        dp_count, dp_sum = new_cnt, new_sum

    print((dp_sum[k][0] + dp_sum[k][1]) % MOD)
