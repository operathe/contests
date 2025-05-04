import collections

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

if sum(A) != N or min(X) != 1:
    print(-1)
    exit()
pairs = sorted(zip(X, A))
cum = 0
for i, (xi, ai) in enumerate(pairs):
    cum += ai
    if cum < xi:
        print(-1)
        exit()

deq = collections.deque()
last = 1
cost = 0

for xi, ai in pairs:
    gap = xi - last
    start = last
    while gap > 0:
        if not deq:
            print(-1)
            exit()
        pos, cnt = deq[0]
        use = min(cnt, gap)
        cost += use * (start - pos) + use * (use - 1) // 2
        start += use
        gap -= use
        cnt -= use
        if cnt == 0:
            deq.popleft()
        else:
            deq[0][1] = cnt
    last = xi + 1
    extra = ai - 1
    if extra > 0:
        deq.append([xi, extra])

if last <= N:
    gap = N - last + 1
    start = last
    while gap > 0:
        if not deq:
            print(-1)
            exit()
        pos, cnt = deq[0]
        use = min(cnt, gap)
        cost += use * (start - pos) + use * (use - 1) // 2
        start += use
        gap -= use
        cnt -= use
        if cnt == 0:
            deq.popleft()
        else:
            deq[0][1] = cnt

print(cost)
