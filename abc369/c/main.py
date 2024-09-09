n = int(input())
a = list(map(int, input().split()))

ans = n
left = 0
while left < n - 1:
    right = left
    diff = a[right + 1] - a[right]
    while right + 1 < n and a[right + 1] - a[right] == diff:
        right += 1
    length = right - left + 1
    ans += length * (length - 1) // 2
    # print(left, right)
    left = right

print(ans)
