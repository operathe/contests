N = 12

ans = 0

for i in range(1, N + 1):
    S = input()
    if len(S) == i:
        ans += 1

print(ans)


# s = [input() for _ in range(12)]
# print(sum([len(s[i]) == i + 1 for i in range(12)]))
