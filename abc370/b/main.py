n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 1

for i in range(n):
    if i > ans - 1:
        ans = a[i][ans - 1]
    else:
        ans = a[ans - 1][i]

print(ans)
