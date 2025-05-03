import bisect

Q = int(input())
times = []
HEAD = 0
ELAPSED = 0
ans = []
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        times.append(ELAPSED)
    elif q[0] == "2":
        ELAPSED += int(q[1])
    else:
        h = int(q[1])
        thresh = ELAPSED - h
        idx = bisect.bisect_right(times, thresh, HEAD, len(times))
        ans.append(str(idx - HEAD))
        HEAD = idx

for a in ans:
    print(a)
