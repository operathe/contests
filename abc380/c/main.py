n, k = map(int, input().split())
s = input().strip()

segments = []
i = 0
while i < n:
    if s[i] == "1":
        st = i
        while i + 1 < n and s[i + 1] == "1":
            i += 1
        ed = i
        segments.append((st, ed))
    i += 1

prev_end = segments[k - 2][1]
st_k, ed_k = segments[k - 1]
length_k = ed_k - st_k + 1

res = []
res.append(s[: prev_end + 1])
res.append("1" * length_k)
res.append("0" * (st_k - prev_end - 1))
res.append(s[ed_k + 1 :])
print("".join(res))
