s = input()
q = int(input())
ks = list(map(int, input().split()))
n = len(s)
out = []
for k in ks:
    k -= 1
    block = k // n
    idx = k % n
    c = s[idx]
    # ブロック番号のビット数が奇数ならケース反転
    if block.bit_count() % 2:
        c = c.swapcase()
    out.append(c)
print(*out)
# print("".join(out))
