s = input().split("|")

a = []

# sの各要素の長さをaに格納
for i in range(len(s)):
    a.append(len(s[i]))

print(*a[1:-1])
