N, M = map(int, input().split())

A = list(map(int, input().split()))

for k in range(N + 1):
    if len(set(A[: N - k])) < M:
        print(k)
        break
