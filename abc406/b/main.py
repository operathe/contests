n, k = map(int, input().split())

A = list(map(int, input().split()))

count = 1
limit_k = 10**k

for a in A:
    if count * a >= limit_k:
        count = 1
    else:
        count *= a

print(count)
