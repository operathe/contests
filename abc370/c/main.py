s, t = input(), input()

n = len(s)

x = []

while s != t:
    nS = "z" * n
    for i in range(n):
        if s[i] != t[i]:
            nS = min(nS, s[:i] + t[i] + s[i + 1 :])
    x.append(nS)
    s = nS

print(len(x))
for x in x:
    print(x)
