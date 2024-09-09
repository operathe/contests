n, k = map(int, (input().split()))
s = [int(input()) for _ in range(n)]

# a の部分数列ですべての要素の値の積がk以下であるような部分数列の個数を求める
# 1. しゃくとり法

ans = 0
right = 0
tmp = 1

if 0 in s:
    print(n)
    exit()

for left in range(n):
    while right < n and tmp * s[right] <= k:
        tmp *= s[right]
        right += 1

    ans = max(ans, right - left)

    if left == right:
        right += 1

    else:
        tmp //= s[left]


print(ans)
