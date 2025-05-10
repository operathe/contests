from functools import lru_cache

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cards = [(v, 0) for v in A] + [(v, 1) for v in B] + [(v, 2) for v in C]
cards.sort(key=lambda x: x[0])
T = len(cards)
full_mask = (1 << T) - 1
v = [cards[i][0] for i in range(T)]
mask_t0 = mask_a0 = 0
for i, (_, g) in enumerate(cards):
    if g == 0:
        mask_t0 |= 1 << i
    elif g == 1:
        mask_a0 |= 1 << i


@lru_cache(None)
def win(mask_t, mask_a, turn):
    mask_cur = mask_t if turn == 0 else mask_a
    if mask_cur == 0:
        return False
    table = full_mask ^ mask_t ^ mask_a
    bs = mask_cur
    while bs:
        lsb_x = bs & -bs
        bs ^= lsb_x
        x = lsb_x.bit_length() - 1
        if turn == 0:
            mt1 = mask_t ^ (1 << x)
            ma1 = mask_a
        else:
            mt1 = mask_t
            ma1 = mask_a ^ (1 << x)
        if not win(mt1, ma1, 1 - turn):
            return True
        t2 = table | (1 << x)
        tb = t2
        while tb:
            lsb_y = tb & -tb
            tb ^= lsb_y
            y = lsb_y.bit_length() - 1
            if v[y] < v[x]:
                if turn == 0:
                    mt2 = mt1 | (1 << y)
                    ma2 = ma1
                else:
                    mt2 = mt1
                    ma2 = ma1 | (1 << y)
                if not win(mt2, ma2, 1 - turn):
                    return True
    return False


res = win(mask_t0, mask_a0, 0)
print("Takahashi" if res else "Aoki")
