n, k = map(int, input().split())

s = input().split("X")

ans = 0
for i in s:
    length = len(i)
    ans += length // k

print(ans)
