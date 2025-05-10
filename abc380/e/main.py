N, Q = map(int, input().split())
parent = list(range(N))
size = [1] * N
leftmost = list(range(N))
rightmost = list(range(N))
color = [i + 1 for i in range(N)]
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    cnt[i] = 1


def find(x):
    """Find the representative (root) of element x with path compression."""
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def unite(a, b):
    """Unite the sets containing a and b by size,
    updating parent, size, and boundaries."""
    a = find(a)
    b = find(b)
    if a == b:
        return a
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    leftmost[a] = min(leftmost[a], leftmost[b])
    rightmost[a] = max(rightmost[a], rightmost[b])
    return a


out = []
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        idx = int(q[1]) - 1
        c_new = int(q[2])
        r = find(idx)
        c_old = color[r]
        if c_old != c_new:
            sz = size[r]
            cnt[c_old] -= sz
            cnt[c_new] += sz
            color[r] = c_new
            leftmost_pos = leftmost[r]
            if leftmost_pos > 0:
                left_root = find(leftmost_pos - 1)
                if color[left_root] == c_new:
                    r = unite(r, left_root)
                    color[r] = c_new
            rightmost_pos = rightmost[r]
            if rightmost_pos < N - 1:
                right_root = find(rightmost_pos + 1)
                if color[right_root] == c_new:
                    r = unite(r, right_root)
                    color[r] = c_new
    else:
        c = int(q[1])
        out.append(str(cnt[c]))
print("\n".join(out))
