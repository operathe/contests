n = int(input())

a = list(map(int, input().split()))

ans = 0
p = 0
for i in a:
    ans += i * p
    p += i
print(ans)
