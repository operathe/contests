N, X, Y = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

a = 0
b = 0

for i in range(N):
    a += A[i]
    b += B[i]

    if a > X or b > Y:
        print(i + 1)
        exit()

print(N)
