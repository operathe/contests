import itertools


N = int(input())

N, M = map(int, input().split())

A = list(map(int, input().split()))

S = []
for i in range(N):
    S.append(int(input()))

A = [list(map(int, input().split())) for _ in range(N)]


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 累積和
cumsum = list(itertools.accumulate(array))
print(*cumsum)

# bitが立っているものだけ取り出す
a_list = [1, 2, 3, 4, 5]
a_bit = [0, 1, 0, 1, 1]

a = list(itertools.compress(a_list, a_bit))
print(a)
