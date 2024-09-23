n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    print(f"数列 {i+1}: {a[i]}")
print(a[0][0])
