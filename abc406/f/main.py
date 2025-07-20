n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

adj = [[] for _ in range(n + 1)]
for i, (u, v) in enumerate(edges, start=1):
    adj[u].append(v)
    adj[v].append(u)

parent = [0] * (n + 1)
tin = [0] * (n + 1)
tout = [0] * (n + 1)
stack = [(1, 0, 0)]
time = 0
while stack:
    u, p, st = stack.pop()
    if st == 0:
        parent[u] = p
        time += 1
        tin[u] = time
        stack.append((u, p, 1))
        for v in adj[u]:
            if v == p:
                continue
            stack.append((v, u, 0))
    else:
        tout[u] = time

child = [0] * n
for i, (u, v) in enumerate(edges, start=1):
    child[i] = u if parent[u] == v else v

size = n
ft = [0] * (n + 1)
for i in range(1, n + 1):
    ft[i] = 1
for i in range(1, n + 1):
    j = i + (i & -i)
    if j <= n:
        ft[j] += ft[i]


def add(i, v):
    while i <= size:
        ft[i] += v
        i += i & -i


def sum_(i):
    s = 0
    while i > 0:
        s += ft[i]
        i -= i & -i
    return s


def range_sum(left, right):
    return sum_(right) - sum_(left - 1)


total = n
ans = []
for cmd in queries:
    if cmd[0] == 1:
        x, w = cmd[1], cmd[2]
        idx = tin[x]
        add(idx, w)
        total += w
    else:
        y = cmd[1]
        v = child[y]
        ssum = range_sum(tin[v], tout[v])
        ans.append(str(abs(total - 2 * ssum)))

for ans in ans:
    print(ans)
