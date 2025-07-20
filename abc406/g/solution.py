import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class SegTree:
    def __init__(self, C):
        self.C = C
        self.m = 100000
        self.N = 2 * self.m
        size = 4 * (self.N + 1)
        self.mn = [0] * size
        self.mx = [0] * size
        self.sum = [0] * size
        self.tagAdd = [0] * size
        self.tagSet = [None] * size
        # backtrack bounds
        self.lpos = []
        self.rpos = []

    def build(self, idx, l, r):
        if l == r:
            v = -self.C if l <= self.m else self.C
            self.mn[idx] = self.mx[idx] = self.sum[idx] = v
        else:
            mid = (l + r) // 2
            self.build(idx * 2, l, mid)
            self.build(idx * 2 + 1, mid + 1, r)
            self._pull(idx)

    def _pull(self, idx):
        lc, rc = idx * 2, idx * 2 + 1
        self.mn[idx] = min(self.mn[lc], self.mn[rc])
        self.mx[idx] = max(self.mx[lc], self.mx[rc])
        self.sum[idx] = self.sum[lc] + self.sum[rc]

    def _apply_set(self, idx, l, r, v):
        self.mn[idx] = self.mx[idx] = v
        self.sum[idx] = v * (r - l + 1)
        self.tagSet[idx] = v
        self.tagAdd[idx] = 0

    def _apply_add(self, idx, l, r, v):
        self.mn[idx] += v
        self.mx[idx] += v
        self.sum[idx] += v * (r - l + 1)
        self.tagAdd[idx] += v

    def _push(self, idx, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        lc, rc = idx * 2, idx * 2 + 1
        if self.tagSet[idx] is not None:
            v = self.tagSet[idx]
            self._apply_set(lc, l, mid, v)
            self._apply_set(rc, mid + 1, r, v)
            self.tagSet[idx] = None
        if self.tagAdd[idx] != 0:
            v = self.tagAdd[idx]
            self._apply_add(lc, l, mid, v)
            self._apply_add(rc, mid + 1, r, v)
            self.tagAdd[idx] = 0

    def updateL(self, idx, l, r, C, i):
        # clamp slopes < -C to -C, record lower bound
        if self.mn[idx] >= -C:
            return 0
        if self.mx[idx] < -C:
            delta = -C * (r - l + 1) - self.sum[idx]
            self._apply_set(idx, l, r, -C)
            # if x in this segment, must pick x >= r
            self.lpos[i] = max(self.lpos[i], r)
            return delta
        self._push(idx, l, r)
        mid = (l + r) // 2
        res = 0
        res += self.updateL(idx * 2, l, mid, C, i)
        res += self.updateL(idx * 2 + 1, mid + 1, r, C, i)
        self._pull(idx)
        return res

    def updateR(self, idx, l, r, C, i):
        # clamp slopes > C to C, record upper bound
        if self.mx[idx] <= C:
            return 0
        if self.mn[idx] > C:
            delta = C * (r - l + 1) - self.sum[idx]
            self._apply_set(idx, l, r, C)
            # if x in this segment, must pick x <= l-1
            self.rpos[i] = min(self.rpos[i], l - 1)
            return delta
        self._push(idx, l, r)
        mid = (l + r) // 2
        res = 0
        res += self.updateR(idx * 2, l, mid, C, i)
        res += self.updateR(idx * 2 + 1, mid + 1, r, C, i)
        self._pull(idx)
        return res

    def modify(self, idx, l, r, ql, qr, v):
        if ql <= l and r <= qr:
            self._apply_add(idx, l, r, v)
            return
        self._push(idx, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.modify(idx * 2, l, mid, ql, qr, v)
        if qr > mid:
            self.modify(idx * 2 + 1, mid + 1, r, ql, qr, v)
        self._pull(idx)

    def query(self, idx, l, r, p):
        if l == r:
            return self.sum[idx]
        self._push(idx, l, r)
        mid = (l + r) // 2
        if p <= mid:
            return self.query(idx * 2, l, mid, p)
        else:
            return self.query(idx * 2 + 1, mid + 1, r, p)


def main():
    N, C, D = map(int, input().split())
    X = list(map(int, input().split()))
    st = SegTree(C)
    m = st.m
    st.lpos = [0] * (N + 1)
    st.rpos = [2 * m] * (N + 1)
    st.build(1, 0, 2 * m)
    # initial F(0)
    sum0 = m * C
    # DP
    for i, x in enumerate(X, 1):
        xi = x + m
        sum0 -= st.updateL(1, 0, 2 * m, C, i)
        sum0 -= st.updateR(1, 0, 2 * m, C, i)
        if xi >= 0:
            st.modify(1, 0, 2 * m, 0, xi, -D)
        if xi + 1 <= 2 * m:
            st.modify(1, 0, 2 * m, xi + 1, 2 * m, +D)
        sum0 += D * xi
    # find minimum
    res = sum0
    cur = sum0
    ans_pos = 0
    for p in range(0, 2 * m + 1):
        cur += st.query(1, 0, 2 * m, p)
        if cur < res:
            res = cur
            ans_pos = p
    # backtrack
    ans = [0] * (N + 1)
    pos = ans_pos
    ans[N] = pos
    for i in range(N, 1, -1):
        pos = max(pos, st.lpos[i])
        pos = min(pos, st.rpos[i])
        ans[i - 1] = pos
    # output
    out = []
    out.append(str(res))
    out.append(" ".join(str(a - m) for a in ans[1:]))
    print("\n".join(out))

if __name__ == '__main__':
    main()
