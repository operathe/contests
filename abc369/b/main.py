n = int(input())
positions = []
for _ in range(n):
    pos, hand = input().split()
    positions.append((int(pos), hand))

ans = 0
last_r = None
last_l = None

for pos, hand in positions:
    if hand == "R":
        if last_r is not None:
            ans += abs(last_r - pos)
        last_r = pos
        # print(last_r)
    elif hand == "L":
        if last_l is not None:
            ans += abs(last_l - pos)
        last_l = pos
# print(last_l)

print(ans)
